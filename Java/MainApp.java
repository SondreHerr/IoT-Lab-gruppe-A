/**
 * Copyright (c) 2015 Digi International Inc.,
 * All rights not expressly granted are reserved.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * Digi International Inc. 11001 Bren Road East, Minnetonka, MN 55343
 * =======================================================================
 */
package com.digi.xdmk.transmitdata;

import java.util.Scanner;

import com.digi.xbee.api.RemoteXBeeDevice;
import com.digi.xbee.api.XBeeDevice;
import com.digi.xbee.api.XBeeNetwork;
import com.digi.xbee.api.exceptions.XBeeException;
import com.digi.xbee.api.listeners.IDataReceiveListener;
import com.digi.xbee.api.models.XBeeMessage;

/**
 * XBee-PRO 900HP DigiMesh Kit Transmit Data Sample application.
 *
 * <p>This sample Java application shows how to send and receive data to/from
 * another XBee devices on the same network using the XBee Java Library.</p>
 *
 * <p>In this example you can send messages to a specific XBee (unicast) or to
 * all (broadcast), following the next pattern:</p>
 * <ul>
 * <li>Unicast: NODE_IDENTIFIER: message</li>
 * <li>Broadcast: ALL: message</li>
 * </ul>
 */
public class MainApp {

    /* Constants */

    // TODO Replace with the port where your module is connected.
    private static final String PORT = "COM1";
    // TODO Replace with the baud rate of your module.
    private static final int BAUD_RATE = 9600;

    private static final Scanner s = new Scanner(System.in);

    private static DataReceiveListener listener = new DataReceiveListener();

    /**
     * Application main method.
     *
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        System.out.println("+----------------------------------------------+");
        System.out.println("|             Transmit Data Sample             |");
        System.out.println("+----------------------------------------------+\n");

        XBeeDevice myDevice = new XBeeDevice(PORT, BAUD_RATE);

        try {
            myDevice.open();

            XBeeNetwork network = myDevice.getNetwork();
            network.startDiscoveryProcess();

            System.out.println("\nLocal XBee: " + myDevice.getNodeID());

            System.out.println("\nScanning the network, please wait...");
            while (network.isDiscoveryRunning()) {
                sleep(100);
            }

            System.out.println("Devices found:");
            for (RemoteXBeeDevice remote : network.getDevices()) {
                System.out.println(" - " + remote.getNodeID());
            }

            System.out.println("\nType your messages here:\n");

            myDevice.addDataListener(listener);

            while (true) {
                try {
                    String[] data = parseData(s.nextLine());

                    if (data[0].toLowerCase().equals("all")) {
                        myDevice.sendBroadcastData(data[1].getBytes());
                    } else {
                        RemoteXBeeDevice remote = network.getDevice(data[0]);
                        if (remote != null) {
                            myDevice.sendData(remote, data[1].getBytes());
                        } else {
                            System.err.println("Could not find the module " + data[0] + " in the network.");
                        }
                    }
                } catch (IndexOutOfBoundsException e) {
                    System.err.println("Error parsing the text. Follow the format <NODE_IDENTIFIER|ALL: message>");
                } catch (XBeeException e) {
                    System.err.println("Error transmitting message: " + e.getMessage());
                }
            }

        } catch (XBeeException e) {
            e.printStackTrace();
            myDevice.close();
            System.exit(1);
        } finally {
            myDevice.close();
            System.exit(0);
        }
    }

    /**
     * Parses the given text to obtain the destination node identifier and the
     * message.
     *
     * @param text Text in the format <NODE_IDENTIFIER|ALL: message>
     * @return String array that contains the node identifier of the remote
     *         device and the message to send.
     */
    private static String[] parseData(String text) throws IndexOutOfBoundsException {
        String[] s = new String[2];
        s[0] = text.substring(0, text.indexOf(":"));
        s[1] = text.substring(text.indexOf(":") + 2);
        return s;
    }

    /**
     * Sleeps the thread for the given milliseconds.
     *
     * @param millis Time to sleep the thread in milliseconds.
     */
    private static void sleep(long millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {}
    }

    /**
     * Class to manage the received data.
     */
    private static class DataReceiveListener implements IDataReceiveListener {
        @Override
        public void dataReceived(XBeeMessage xbeeMessage) {
            System.out.println("------------------------------------------------------------------");
            System.out.println("> " + xbeeMessage.getDevice().getNodeID() +
                    (xbeeMessage.isBroadcast() ? " (broadcast)" : "") +
                    ": " + new String(xbeeMessage.getData()));
            System.out.println("------------------------------------------------------------------");
        }
    }

}