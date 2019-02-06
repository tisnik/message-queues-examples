import org.zeromq.ZMQ;
import org.zeromq.ZContext;

public class Client
{

    static void send_request(ZMQ.Socket socket, int number)
    {
        String request = String.valueOf(number);

        socket.send(request.getBytes(ZMQ.CHARSET), 0);
        System.out.println("Sent: " + request);

        byte[] raw_response = socket.recv(0);
        String response = new String(raw_response, ZMQ.CHARSET);
        System.out.println("Received from server: " + response);
    }

    public static void main(String[] args) throws Exception
    {
        try (ZContext context = new ZContext()) {
            ZMQ.Socket socket = context.createSocket(ZMQ.REQ);
            socket.connect("tcp://localhost:5555");
            for (int i=0; i<10; i++) {
                send_request(socket, i);
            }
            send_request(socket, -10);
        }
    }
}
