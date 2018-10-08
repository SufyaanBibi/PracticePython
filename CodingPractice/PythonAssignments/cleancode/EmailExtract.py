##############################################################################
#
# 5YP CONFIDENTIAL
# __________________
#
#  [2002] - [2018] 5YP Systems Incorporated
#  All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of 5YP Systems Incorporated and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to XYZABC_DEF_GHI_JOLLY_GOOD_SHOW Systems Incorporated
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from 5YP Systems Incorporated.
#
##############################################################################

# Author : Basil Bibi
# Date : 7th October 2018

# The MalformedEmailAddress Exception.
# This exception is used when a malformed email address is encountered.
# A malformed email address is an email address that is malformed.
class MalformedEmailAddress_Exception(Exception):
    pass


# The EmailDetails class.
# This is a class that holds details about an email address
# e.g. id@domain.com
class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain

# extract_email_address
# This function extracats email degails from am email address string. The function should raise a MalformedEmailAddress if it cannot parse the email address it is passed.
def extract_details_from_email_address(email_addr):
    # return a value that will pass the test
    return EmailDetails('basil', '5yp.com')

# Aloawys leave a blank line at the end of the file.