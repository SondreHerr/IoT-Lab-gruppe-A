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
package com.digi.xbee.api.exceptions;

/**
 * This exception will be thrown when trying to perform any operation with 
 * the XBee device and its communication interface is closed.
 * 
 * @see RuntimeException
 */
public class InterfaceNotOpenException extends RuntimeException {

	// Constants
	private static final long serialVersionUID = 1L;
	private static final String DEFAULT_MESSAGE = "The connection interface is not open.";

	/**
	 * Creates an {@code InterfaceNotOpenException} with 
	 * {@value #DEFAULT_MESSAGE} as its error detail message.
	 */
	public InterfaceNotOpenException() {
		super(DEFAULT_MESSAGE);
	}
	
	/**
	 * Creates an {@code InterfaceNotOpenException} with the specified 
	 * message.
	 * 
	 * @param message The associated message.
	 */
	public InterfaceNotOpenException(String message) {
		super(message);
	}
	
	/**
	 * Creates an {@code InterfaceNotOpenException} with the specified message
	 * and cause.
	 * 
	 * @param message The associated message.
	 * @param cause The cause of this exception.
	 * 
	 * @see Throwable
	 */
	public InterfaceNotOpenException(String message, Throwable cause) {
		super(message, cause);
	}
}
