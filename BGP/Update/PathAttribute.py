#
# This file is part of PCAP BGP Parser (pbgpp)
#
# Copyright 2016 DE-CIX Management GmbH
# Author: Tobias Hannaske <tobias.hannaske@de-cix.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from BGP.Statics import BGPStatics
from BGP.Translation import BGPTranslation


class BGPPathAttribute:
    def __init__(self, payload):
        self.payload = payload

        self.type = None
        self.error = None
        self.parsed = False

    def __str__(self):
        return ""

    def json(self):
        return {
            "type": self.type,
            "type_string": BGPTranslation.path_attribute(self.type),
            "error": self.error,
        }

    @staticmethod
    def factory(attribute_type, payload, attribute_flags):
        # Factory pattern for the path attributes of UPDATE message
        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_ADVERTISER:
            from BGP.Update.PathAttributes.Advertiser import PathAttributeAdvertiser
            return PathAttributeAdvertiser(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_AGGREGATOR:
            from BGP.Update.PathAttributes.Aggregator import PathAttributeAggregator
            return PathAttributeAggregator(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_AIGP:
            from BGP.Update.PathAttributes.AIGP import PathAttributeAIGP
            return PathAttributeAIGP(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_AS4_AGGREGATOR:
            from BGP.Update.PathAttributes.AS4Aggregator import PathAttributeAS4Aggregator
            return PathAttributeAS4Aggregator(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_AS4_PATH:
            from BGP.Update.PathAttributes.AS4Path import PathAttributeAS4Path
            return PathAttributeAS4Path(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_AS_PATHLIMIT:
            from BGP.Update.PathAttributes.ASPathLimit import PathAttributeASPathLimit
            return PathAttributeASPathLimit(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_AS_PATH:
            from BGP.Update.PathAttributes.ASPath import PathAttributeASPath
            return PathAttributeASPath(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_ATOMIC_AGGREGATE:
            from BGP.Update.PathAttributes.AtomicAggregate import PathAttributeAtomicAggregate
            return PathAttributeAtomicAggregate(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_ATTR_SET:
            from BGP.Update.PathAttributes.AttributeSet import PathAttributeAttributeSet
            return PathAttributeAttributeSet(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_BGP_ENTROPY_LABEL_CAPABILITY:
            from BGP.Update.PathAttributes.BGPEntropyLabelCapability import PathAttributeBGPEntropyLabelCapability
            return PathAttributeBGPEntropyLabelCapability(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_BGP_LS:
            from BGP.Update.PathAttributes.BGPLS import PathAttributeBGPLS
            return PathAttributeBGPLS(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_CLUSTER_LIST:
            from BGP.Update.PathAttributes.ClusterList import PathAttributeClusterList
            return PathAttributeClusterList(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_COMMUNITIES:
            from BGP.Update.PathAttributes.Communities import PathAttributeCommunities
            return PathAttributeCommunities(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_CONNECTOR_ATTRIBUTE:
            from BGP.Update.PathAttributes.ConnectorAttribute import PathAttributeConnectorAttribute
            return PathAttributeConnectorAttribute(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_DPA:
            from BGP.Update.PathAttributes.DPA import PathAttributeDPA
            return PathAttributeDPA(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_EXTENDED_COMMUNITIES:
            from BGP.Update.PathAttributes.ExtendedCommunities import PathAttributeExtendedCommunities
            return PathAttributeExtendedCommunities(payload, attribute_flags)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_IPV6_ADDRESS_SPECIFIC_EXTENDED_COMMUNITY:
            from BGP.Update.PathAttributes.IPv6AddressSpecificExtendedCommunity import PathAttributeIPv6AddressSpecificExtendedCommunitiy
            return PathAttributeIPv6AddressSpecificExtendedCommunitiy(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_LOCAL_PREF:
            from BGP.Update.PathAttributes.LocalPreferences import PathAttributeLocalPreferences
            return PathAttributeLocalPreferences(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_MP_REACH_NLRI:
            from BGP.Update.PathAttributes.MPReachNLRI import PathAttributeMPReachNLRI
            return PathAttributeMPReachNLRI(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_MP_UNREACH_NLRI:
            from BGP.Update.PathAttributes.MPUnReachNLRI import PathAttributeMPUnReachNLRI
            return PathAttributeMPUnReachNLRI(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_MULTI_EXIT_DISC:
            from BGP.Update.PathAttributes.MultipleExitDiscriminator import PathAttributeMultipleExitDiscriminator
            return PathAttributeMultipleExitDiscriminator(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_NEXT_HOP:
            from BGP.Update.PathAttributes.NextHop import PathAttributeNextHop
            return PathAttributeNextHop(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_ORIGIN:
            from BGP.Update.PathAttributes.Origin import PathAttributeOrigin
            return PathAttributeOrigin(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_ORIGINATOR_ID:
            from BGP.Update.PathAttributes.OriginatorID import PathAttributeOriginatorID
            return PathAttributeOriginatorID(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_PE_DISTINGUISHER_LABLES:
            from BGP.Update.PathAttributes.PEDistinguisherLabels import PathAttributePEDistinguisherLabels
            return PathAttributePEDistinguisherLabels(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_PMSI_TUNNEL:
            from BGP.Update.PathAttributes.PMSITunnel import PathAttributePMSITunnel
            return PathAttributePMSITunnel(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_RCID_PATH_CLUSTER_ID:
            from BGP.Update.PathAttributes.PMSITunnel import PathAttributePMSITunnel
            return PathAttributePMSITunnel(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_RESERVED:
            from BGP.Update.PathAttributes.Reserved import PathAttributeReserved
            return PathAttributeReserved(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_RESERVED_DEVELOPMENT:
            from BGP.Update.PathAttributes.ReservedDevelopment import PathAttributeReservedDevelopment
            return PathAttributeReservedDevelopment(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_SAFI_SSA:
            from BGP.Update.PathAttributes.SAFISSA import PathAttributeSAFISSA
            return PathAttributeSAFISSA(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_TRAFFIC_ENGINEERING:
            from BGP.Update.PathAttributes.TrafficEngineering import PathAttributeTrafficEngineering
            return PathAttributeTrafficEngineering(payload)

        if attribute_type == BGPStatics.UPDATE_ATTRIBUTE_TUNNEL_ENCAPSULATION:
            from BGP.Update.PathAttributes.TunnelEncapsulation import PathAttributeTunnelEncapsulation
            return PathAttributeTunnelEncapsulation(payload)

        from BGP.Update.PathAttributes.Unknown import PathAttributeUnknown
        return PathAttributeUnknown(payload)
