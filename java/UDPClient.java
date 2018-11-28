
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UDPClient {
	private final static int PORT = 5000;
	private static final String HOSTNAME = "localhost";
	public static void main(String[] args) {
		System.out.println("This is the UDP Client.");
		try {
			DatagramSocket socket = new DatagramSocket(0);
			Scanner scanner = new Scanner(System.in);
         System.out.println("Type a line");
			String requestString = scanner.nextLine();
			scanner.close();
			byte[] requestBuffer = requestString.getBytes();
         System.out.println(requestBuffer);
			InetAddress host = InetAddress.getByName(HOSTNAME);

			DatagramPacket request = new DatagramPacket(requestBuffer, requestBuffer.length, host, PORT);
			socket.send(request);
			
			DatagramPacket response = new DatagramPacket(new byte[1024], 1024);
			socket.receive(response);
			String result = new String(response.getData());
			System.out.println(result);
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}
}
