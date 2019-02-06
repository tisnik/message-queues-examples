import org.zeromq.ZMQ;
import org.zeromq.ZContext;

public class Consumer
{
    static final int PORT = 5555;

    static void receive_messages(ZMQ.Socket socket)
    {
        int cnt = 0;
        while (true) {
            byte[] raw_message = socket.recv(0);
            cnt++;
            String message = new String(raw_message, ZMQ.CHARSET);
            System.out.println("Received message: " + message);
        }
    }

    public static void main(String[] args) throws Exception
    {
        try (ZContext context = new ZContext()) {
            ZMQ.Socket socket = context.createSocket(ZMQ.PULL);

            String address = "tcp://localhost:" + PORT;
            socket.connect(address);
            System.out.println("Connected to " + address);

            System.out.println("Waiting for message...");

            receive_messages(socket);
        }
    }
}
