import org.zeromq.ZMQ;
import org.zeromq.ZContext;

public class Producer
{
    static final int PORT = 5555;

    static void send_message(ZMQ.Socket socket, String message)
    {
        socket.send(message.getBytes(ZMQ.CHARSET), 0);
    }

    public static void main(String[] args) throws Exception
    {
        try (ZContext context = new ZContext()) {
            ZMQ.Socket socket = context.createSocket(ZMQ.PUSH);

            String address = "tcp://*:" + PORT;
            socket.bind(address);
            System.out.println("Bound to address " + address);

            for (int i=0; i<100; i++) {
                String message = "Messsage #" + i;
                send_message(socket, message);
                try {
                    Thread.sleep(50);
                }
                catch (InterruptedException e) {
                    System.out.println("Interrupted");
                    return;
                }
            }
        }
    }
}
