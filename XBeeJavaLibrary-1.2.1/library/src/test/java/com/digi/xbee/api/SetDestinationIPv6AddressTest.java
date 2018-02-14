/**
 * Copyright 2017, Digi International Inc.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, you can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES 
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF 
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR 
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN 
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF 
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */
package com.digi.xbee.api;

import java.net.Inet6Address;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;

import com.digi.xbee.api.connection.serial.SerialPortRxTx;
import com.digi.xbee.api.exceptions.ATCommandException;
import com.digi.xbee.api.exceptions.InterfaceNotOpenException;
import com.digi.xbee.api.exceptions.InvalidOperatingModeException;
import com.digi.xbee.api.exceptions.TimeoutException;
import com.digi.xbee.api.exceptions.XBeeException;

public class SetDestinationIPv6AddressTest {

	// Constants.
	private static final String PARAMETER = "DL";

	private static Inet6Address ADDRESS;

	// Variables.
	private ThreadDevice xbeeDevice;

	@Before
	public void setup() throws Exception {
		ADDRESS = (Inet6Address) Inet6Address.getByName("FDB3:0001:0002:0000:0004:0005:0006:0007");

		// Instantiate a local Thread device object.
		xbeeDevice = PowerMockito.spy(new ThreadDevice(Mockito.mock(SerialPortRxTx.class)));
	}

	/**
	 * Test method for {@link com.digi.xbee.api.AbstractXBeeDevice#setIPv6DestinationAddress(Inet6Address)}.
	 *
	 * <p>Verify that the destination IPv6 address of an XBee device cannot be set
	 * if the destination IPv6 address is null.</p>
	 *
	 * @throws XBeeException
	 */
	@Test(expected=NullPointerException.class)
	public void testSetIPv6DestinationAddressErrorNullAddress() throws XBeeException {
		// Set the destination IPv6 address.
		xbeeDevice.setIPv6DestinationAddress(null);
	}

	/**
	 * Test method for {@link com.digi.xbee.api.AbstractXBeeDevice#setIPv6DestinationAddress(Inet6Address)}.
	 *
	 * <p>Verify that the destination IPv6 address of an XBee device cannot be set
	 * if the connection of the device is closed.</p>
	 *
	 * @throws XBeeException
	 */
	@Test(expected=InterfaceNotOpenException.class)
	public void testSetDestinationIPv6AddressErrorConnectionClosed() throws XBeeException {
		// Throw an interface not open exception when trying to set any parameter.
		Mockito.doThrow(new InterfaceNotOpenException()).when(xbeeDevice).setParameter(Mockito.anyString(), Mockito.any(byte[].class));

		// Set the destination IPv6 address.
		xbeeDevice.setIPv6DestinationAddress(ADDRESS);
	}

	/**
	 * Test method for {@link com.digi.xbee.api.AbstractXBeeDevice#setIPv6DestinationAddress(Inet6Address)}.
	 *
	 * <p>Verify that the destination IPv6 address of an XBee device cannot be set
	 * if the operating mode of the device is not valid.</p>
	 *
	 * @throws XBeeException
	 */
	@Test(expected=InvalidOperatingModeException.class)
	public void testSetDestinationIPv6AddressErrorInvalidOperatingMode() throws XBeeException {
		// Throw an invalid operating mode exception when trying to set any parameter.
		Mockito.doThrow(new InvalidOperatingModeException()).when(xbeeDevice).setParameter(Mockito.anyString(), Mockito.any(byte[].class));

		// Set the destination IPv6 address.
		xbeeDevice.setIPv6DestinationAddress(ADDRESS);
	}

	/**
	 * Test method for {@link com.digi.xbee.api.AbstractXBeeDevice#setIPv6DestinationAddress(Inet6Address)}.
	 *
	 * <p>Verify that the destination IPv6 address of an XBee device cannot be set if there is a timeout setting
	 * the DL parameter of the address.</p>
	 *
	 * @throws XBeeException
	 */
	@Test(expected=TimeoutException.class)
	public void testSetDestinationIPv6AddressDLErrorTimeout() throws XBeeException {
		// Throw a timeout exception when trying to set the DL parameter.
		Mockito.doThrow(new TimeoutException()).when(xbeeDevice).setParameter(Mockito.eq(PARAMETER), Mockito.any(byte[].class));

		// Set the destination IPv6 address.
		xbeeDevice.setIPv6DestinationAddress(ADDRESS);
	}

	/**
	 * Test method for {@link com.digi.xbee.api.AbstractXBeeDevice#setIPv6DestinationAddress(Inet6Address)}.
	 *
	 * <p>Verify that the destination IPv6 address of an XBee device cannot be set
	 * if the answer when setting the DL parameter is null or the response
	 * status is not OK. It is, there is an AT command exception setting the DL
	 * parameter.</p>
	 *
	 * @throws XBeeException
	 */
	@Test(expected=ATCommandException.class)
	public void testSetDestinationIPv6AddressDLErrorInvalidAnswer() throws XBeeException {
		// Throw an AT command exception when trying to set the DL parameter.
		Mockito.doThrow(new ATCommandException(null)).when(xbeeDevice).setParameter(Mockito.eq(PARAMETER), Mockito.any(byte[].class));

		// Set the destination IPv6 address.
		xbeeDevice.setIPv6DestinationAddress(ADDRESS);
	}

	/**
	 * Test method for {@link com.digi.xbee.api.AbstractXBeeDevice#setIPv6DestinationAddress(Inet6Address)}.
	 *
	 * <p>Verify that the destination IPv6 address of an XBee device can be set
	 * successfully.</p>
	 *
	 * @throws XBeeException
	 */
	@Test
	public void testSetDestinationIPv6AddressSuccess() throws XBeeException {
		// Do nothing when trying to set the DL parameter.
		Mockito.doNothing().when(xbeeDevice).setParameter(Mockito.eq(PARAMETER), Mockito.any(byte[].class));

		// Set the destination IPv6 address.
		xbeeDevice.setIPv6DestinationAddress(ADDRESS);
	}
}
