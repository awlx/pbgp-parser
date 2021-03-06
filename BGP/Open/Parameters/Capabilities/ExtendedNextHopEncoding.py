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

from BGP.Open.Parameters.Capability import BGPCapability
from BGP.Statics import BGPStatics


class CapabilityExtendedNextHopEncoding(BGPCapability):
    def __init__(self, payload):
        BGPCapability.__init__(self, payload)
        self.type = BGPStatics.CAPABILITY_EXTENDED_NEXT_HOP_ENCODING
        self.__parse()

    def __parse(self):
        self.parsed = True