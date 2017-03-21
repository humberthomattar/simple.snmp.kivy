from pysnmp.hlapi import *
from os import *

class SimpleSnmp():
    try:
        def __init__(self, ip, community, porta):
           self.ip = str(ip)
           self.community = community
           self.porta = int(porta)
    except:
        pass
    def GetSNMP(self):
        try:
            resultado = errorIndication, errorStatus, errorIndex, varBinds = next(
                getCmd(SnmpEngine(),
                    CommunityData(self.community, mpModel=0),
                    UdpTransportTarget((self.ip, self.porta)),
                    ContextData(),
                    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
                    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)),
                    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact', 0)),
                    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0))
                    ))
            if errorIndication:
                return str(errorIndication)
            elif errorStatus:
                return str('%s at %s' % (errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            else:
                g = ''
                for varBind in varBinds:
                    g = g + (' = '.join([x.prettyPrint() for x in varBind])) + '\n'
                return str(g)
        except Exception as e:
            return str(e)
