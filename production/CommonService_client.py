##################################################
# file: CommonService_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/local/bin/wsdl2py common.asmx.xml
# 
##################################################

from CommonService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class CommonServiceLocator:
    CommonServiceSoap_address = "http://common.virtualearth.net/find-30/common.asmx"
    def getCommonServiceSoapAddress(self):
        return CommonServiceLocator.CommonServiceSoap_address
    def getCommonServiceSoap(self, url=None, **kw):
        return CommonServiceSoapSOAP(url or CommonServiceLocator.CommonServiceSoap_address, **kw)

# Methods
class CommonServiceSoapSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: GetVersionInfo
    def GetVersionInfo(self, request, soapheaders=(), **kw):
        if isinstance(request, GetVersionInfoSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.Send(None, None, request, soapaction="http://s.mappoint.net/mappoint-30/GetVersionInfo", soapheaders=soapheaders, **kw)
        # no output wsaction
        response = self.binding.Receive(GetVersionInfoSoapOut.typecode)
        return response

    # op: GetCountryRegionInfo
    def GetCountryRegionInfo(self, request, soapheaders=(), **kw):
        if isinstance(request, GetCountryRegionInfoSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.Send(None, None, request, soapaction="http://s.mappoint.net/mappoint-30/GetCountryRegionInfo", soapheaders=soapheaders, **kw)
        # no output wsaction
        response = self.binding.Receive(GetCountryRegionInfoSoapOut.typecode)
        return response

    # op: GetEntityTypes
    def GetEntityTypes(self, request, soapheaders=(), **kw):
        if isinstance(request, GetEntityTypesSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.Send(None, None, request, soapaction="http://s.mappoint.net/mappoint-30/GetEntityTypes", soapheaders=soapheaders, **kw)
        # no output wsaction
        response = self.binding.Receive(GetEntityTypesSoapOut.typecode)
        return response

    # op: GetDataSourceInfo
    def GetDataSourceInfo(self, request, soapheaders=(), **kw):
        if isinstance(request, GetDataSourceInfoSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.Send(None, None, request, soapaction="http://s.mappoint.net/mappoint-30/GetDataSourceInfo", soapheaders=soapheaders, **kw)
        # no output wsaction
        response = self.binding.Receive(GetDataSourceInfoSoapOut.typecode)
        return response

    # op: GetGreatCircleDistances
    def GetGreatCircleDistances(self, request, soapheaders=(), **kw):
        if isinstance(request, GetGreatCircleDistancesSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.Send(None, None, request, soapaction="http://s.mappoint.net/mappoint-30/GetGreatCircleDistances", soapheaders=soapheaders, **kw)
        # no output wsaction
        response = self.binding.Receive(GetGreatCircleDistancesSoapOut.typecode)
        return response

    # op: GetClientToken
    def GetClientToken(self, request, soapheaders=(), **kw):
        if isinstance(request, GetClientTokenSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.Send(None, None, request, soapaction="http://s.mappoint.net/mappoint-30/GetClientToken", soapheaders=soapheaders, **kw)
        # no output wsaction
        response = self.binding.Receive(GetClientTokenSoapOut.typecode)
        return response

GetVersionInfoSoapIn = GED("http://s.mappoint.net/mappoint-30/", "GetVersionInfo").pyclass

GetVersionInfoSoapOut = GED("http://s.mappoint.net/mappoint-30/", "GetVersionInfoResponse").pyclass

GetCountryRegionInfoSoapIn = GED("http://s.mappoint.net/mappoint-30/", "GetCountryRegionInfo").pyclass

GetCountryRegionInfoSoapOut = GED("http://s.mappoint.net/mappoint-30/", "GetCountryRegionInfoResponse").pyclass

GetEntityTypesSoapIn = GED("http://s.mappoint.net/mappoint-30/", "GetEntityTypes").pyclass

GetEntityTypesSoapOut = GED("http://s.mappoint.net/mappoint-30/", "GetEntityTypesResponse").pyclass

GetDataSourceInfoSoapIn = GED("http://s.mappoint.net/mappoint-30/", "GetDataSourceInfo").pyclass

GetDataSourceInfoSoapOut = GED("http://s.mappoint.net/mappoint-30/", "GetDataSourceInfoResponse").pyclass

GetGreatCircleDistancesSoapIn = GED("http://s.mappoint.net/mappoint-30/", "GetGreatCircleDistances").pyclass

GetGreatCircleDistancesSoapOut = GED("http://s.mappoint.net/mappoint-30/", "GetGreatCircleDistancesResponse").pyclass

GetClientTokenSoapIn = GED("http://s.mappoint.net/mappoint-30/", "GetClientToken").pyclass

GetClientTokenSoapOut = GED("http://s.mappoint.net/mappoint-30/", "GetClientTokenResponse").pyclass
