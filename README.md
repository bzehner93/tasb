The library provides a proof-of-concept for integration testing of a SPP interface.

## Description ##
Bluetooth® wireless technology (Bluetooth® is a registered Trademark of the Bluetooth Special Interest Group) is a well established technology in a variety of applications in the industrial and private environment. Bluetooth
is ideal for implementing distributed applications. One possible interface for this
is the so-called ’Serial Port Profile‘ (SPP), which can be used to establish a serial
connection via a radio link. 
A system distributed via Bluetooth typically consists of several modules, which
may be developed independently by different suppliers.

The infrastructure and software objects included in the ***tasb software*** provide the
base for efficient integration testing of software module interfaces communicating
through the Serial Port Profile.

## Installation ##
This software requires the python runtime including the pybluez addon.

Please refer to
https://docs.python.org/3/using/windows.html

for setting up python 3.5.
Refer to 
https://github.com/pybluez/pybluez
for the required pybluez addon.

## Usage ##
The following sample script shows how the library may be used.
```python
# Configure RFCOMM connection
connection = TasbConnection(server_address, service_port, time_out)
connection.setCommandLoggingEnabled(True)

#Create testSuite
test_suite = TasbTestSuite(connection)

# Create the stream decorator that will manage pings
stream_decorator = TasbPingAcknowledgeDecorator(ping_request, ping_confirm)

# First test
action = TasbAction(anyCommand)
condition = TasbAnyEndingCondition(anyCommand)
test = TasbActionAndConditionTest(action, condition, "SampleTest")

# Time lock after test
time_lock1 = TasbTestDelay(2)

# Add the tests to the test_suite
test_suite.add(stream_decorator).add(test).add(time_lock1).add(TasbSuiteFinalizer())

# Execute testSuite
print("Running...")
test_suite.run()
```

## License ##
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

**PyBluez**
The addon is used in its unmodified version to establish communcition with the bluetooth drivers on the target linux host. The addon is published under the terms of the GNU General Public License
