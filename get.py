from pysnmp.hlapi import *
from os import *
import oid

class SimpleSnmp():
    try:
        def __init__(self, ip, community):
           self.ip = ip
           self.community = community
    except:
        pass
    def GetSNMP(self):
        try:
    		g = errorIndication, errorStatus, errorIndex, varBinds = next(
    		    getCmd(SnmpEngine(),
    		    CommunityData(self.community),
    		    UdpTransportTarget((self.ip, 161)),
    		    ContextData(),
    		    ObjectType(ObjectIdentity(oid.Descr)),
    		    ObjectType(ObjectIdentity(oid.UpTime)),
    		    ObjectType(ObjectIdentity(oid.Contact)),
    		    ObjectType(ObjectIdentity(oid.Name)),
    		    ObjectType(ObjectIdentity(oid.ObjectID)),
    		    ObjectType(ObjectIdentity(oid.Location)),
    		    ObjectType(ObjectIdentity(oid.Services)),
    			),)
    		if errorIndication:
    		    return str(errorIndication)
    		elif errorStatus:
    		    return str('%s at %s' % (errorStatus.prettyPrint(),
    				        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    		else:
    		    return str(g)
        except Exception as e:
            return str(e)
