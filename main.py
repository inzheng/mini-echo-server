#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
        <html>
            <body>
                <form action = "/print"  method = "post"> 
                    <p>Please Enter your Name</p>
                    Name: <input type = "text" name = "user_name">
                    <input type = "submit" value = "Send">
                </form>    
            </body>
        </html>
        """)

class PrintHandler(webapp2.RequestHandler):
    def post(self):
        user_name = self.request.get('user_name')
        response = " <html><body>"
        response += "<p>Your name is "
        response += user_name
        response += "</p></body></html>"
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/print', PrintHandler),
], debug=True)
