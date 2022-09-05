What is this?
=============
Scripts to demonstrate the remote procedure call functionality between Linux and Arduino sides of the Portenta x8.

Inspired by this official Arduino tutorial:
`Data Exchange Between Python on Linux and an Arduino Sketch <https://docs.arduino.cc/tutorials/portenta-x8/python-arduino-data-exchange>`_

Rather than relying on connected sensors to see RPC output, this script simply blinks the built-in LED on / off and counts up from 0.

Install steps
=============
Arduino side
------------

1. `Upload the arduino-blink-rpc sketch to the x8 <https://docs.arduino.cc/tutorials/portenta-x8/uploading-sketches-m4>`_
1. Built-in LED should start blinking.

Linux side
----------
1. Load python script directory onto x8 using `adb <https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box#adb>`_ on your PC

.. code-block:: console

    adb push python-blink-rpc /home/fio

2. Build the Docker image with docker-compose on the x8

.. code-block:: console

    cd /home/fio/python-blink-rpc
    sudo docker-compose build

3. Run the container

.. code-block:: console

    sudo docker-compose up

4. You should see output like this

.. code-block:: console

    python-blink-rpc_1  |
    python-blink-rpc_1  | ============================================
    python-blink-rpc_1  | ==       Portenta X8 M4 output            ==
    python-blink-rpc_1  | ============================================
    python-blink-rpc_1  |
    python-blink-rpc_1  | count:  1
    python-blink-rpc_1  | led:  1
    python-blink-rpc_1  | count:  2
    python-blink-rpc_1  | led:  0
    python-blink-rpc_1  | count:  3
    python-blink-rpc_1  | led:  1
