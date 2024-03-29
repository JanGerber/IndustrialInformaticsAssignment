import datetime
import json
import logging
import threading

from flask import Flask, render_template
from flask import request

from industrial_informatic_assigment.monitoring.monitoring_alarm_dao import MonitoringAlarmDAO
from industrial_informatic_assigment.monitoring.monitoring_event_dao import MonitoringEventDAO
from industrial_informatic_assigment.monitoring.monitoring_service import MonitoringService
from industrial_informatic_assigment.workstation.subsciber import Subscriber
from industrial_informatic_assigment.workstation.workstation import Workstation

# Logging
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Workstation
w2BaseUrl = "http://192.168.2"
ws = Workstation(w2BaseUrl, None)

# Subscriber
locPort = 5000
serverAddress = "http://192.168.101.200:" + str(locPort)
subscriber = Subscriber(serverAddress)
subscriber.subscribeToAllEventsOfWsSimple(ws)

# DB
eventDAO = MonitoringEventDAO(False)
alarmDAO = MonitoringAlarmDAO(False)

# Service
monitoringService = MonitoringService(eventDAO, alarmDAO)

app = Flask(__name__)


@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)


@app.route('/rest/ws/<string:wsId>/event', methods=['POST'])
def index(wsId):
    eventDesc = request.json

    serverTime = datetime.datetime.now()
    eventDic = {"eventID": eventDesc['id'], "ws": wsId, "senderID": eventDesc['senderID'],
                "payload": eventDesc['payload'], "serverTime": serverTime}
    monitoringService.insert_event(eventDic)

    resp = json.dumps({'thank': 'yes'}), 200, {'ContentType': 'application/json'}
    return resp


@app.route('/rest/events', methods=['POST'])
def getEvents():
    # logging.debug("Retrieving all the events...")
    events = request.json
    if events["timestampnewer"] == "":
        allEvents = monitoringService.getAllEvents()
    else:
        allEvents = monitoringService.getEventsNewerThen(events["timestampnewer"])
    allEventsJson = json.dumps(allEvents)
    return allEventsJson


@app.route('/rest/ws/status', methods=['GET'])
def getWsStatus():
    status = monitoringService.getStatusOfWS()
    cnvMsg_str = json.dumps(vars(status))
    return cnvMsg_str


@app.route('/rest/alarm', methods=['GET'])
def getAllAlarms():
    alarms = monitoringService.getAllAlarms()
    cnvMsg_str = json.dumps(alarms)
    return cnvMsg_str


@app.route('/rest/alarm/new', methods=['POST'])
def getAllNewAlarms():
    eventDesc = request.json
    alarmId = eventDesc['alarmId']
    alarms = monitoringService.getAllNewAlarms(alarmId)
    cnvMsg_str = json.dumps(alarms)
    return cnvMsg_str


def checkTimeElapsedAlarms():
    monitoringService.checkForNewAlarms()
    threading.Timer(5.0, checkTimeElapsedAlarms).start()


if __name__ == '__main__':
    checkTimeElapsedAlarms()

    app.run("0.0.0.0", locPort)
