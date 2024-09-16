
Sample Rates
===================

The sampling rate "Hz" of sensors data, the smoothing of the data, then fusing sensor data streams together determines
the speed your robot can safely run autonomously.

Since the amount of work a robot can do is based on it's top speed.
Faster means large area covered but also all the engineering trade offs to go faster.

The sample_rate, engineering balance is why autonomous drones are not cost effect with 2024 technology
but surface vehicles can be fully autonomous,where cost and weight are not so critical.


Example.
2.6 meters per second a fast walk and is 10km kilometers per hour.
a 10hz sample rate covers 0.26m
at a faster speed of 50km per hour is now 1.3m  a RC car top speed at 10hz.
at highway speed  of 100km  is now 2.6m at 10hz

.. note::
   a raspberry pi can do video sampling at rates 7-10 Hz.


+------------------------+---------------+----------+----------------+-----------------+
| Sample Rate  Hz        | Speed meters  | Speed km | Meters between | 5 seconds       |
| samples per second     | per second    | per hour | samples        | meters traveled |
+========================+===============+==========+================+=================+
| 10hz                   |  2.6          |  10km    |    0.26        |   13m           |
+------------------------+---------------+----------+----------------+-----------------+
| 10hz                   | 13.0          |  50km    |    1.3         |   65m           |
+------------------------+---------------+----------+----------------+-----------------+
| 10hz                   | 26.0          | 100km    |    2.6         |  130m           |
+------------------------+---------------+----------+----------------+-----------------+

The sample rate  translated into cpu cycles to publish sensor messages into ROS and for subscribers to see and act upon the newly published messages
It is critical to make sure that the published messages are processed as quickly as possible.

Since we are running on docker containers on a interrupt driven OS. Timing of important decisions must be taken into account.
ROS 2 uses a DDS that can enforce a QoS "Quality of Service" for important messages, to help deal with decision timing.

.. seealso::
   ROS 2 Jazzy  Quality of Service
    https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html




Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.