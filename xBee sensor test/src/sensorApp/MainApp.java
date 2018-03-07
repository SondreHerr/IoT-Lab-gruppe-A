package sensorApp;

import com.digi.xbee.api.WiFiDevice;
import com.digi.xbee.api.XBeeDevice;
import com.digi.xbee.api.exceptions.XBeeException;
import com.digi.xbee.api.models.XBeeProtocol;
public class MainApp {
	/* Constants */
	// TODO
	private static final String PORT = "usbserial-AL033DVI";
	// TODO
	private static final int BAUD_RATE = 9600;

	private static final String DATA_TO_SEND = "Hello XBee World!";
	
	public static void main(String[] args) {
		
		XBeeDevice myDevice = new XBeeDevice(PORT, BAUD_RATE);
		byte[] dataToSend = DATA_TO_SEND.getBytes();
		
		try {
			myDevice.open();
			System.out.format("Sending broadcast data: '%s'", new String
					(dataToSend));
			if (myDevice.getXBeeProtocol() == XBeeProtocol.XBEE_WIFI) {
				myDevice.close();
				myDevice = new WiFiDevice(PORT, BAUD_RATE);
				myDevice.open();
				((WiFiDevice)myDevice).sendBroadcastIPData(0x2616, dataToSend);
			} else
				myDevice.sendBroadcastData(dataToSend);
			System.out.println(" >> Success");
		} catch (XBeeException e) {
			System.out.println(" >> Error");
			e.printStackTrace();
			System.exit(1);
		} finally {
			myDevice.close();
		}
		
	}
}
