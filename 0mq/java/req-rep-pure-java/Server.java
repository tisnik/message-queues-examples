import org.zeromq.ZMQ;
import org.zeromq.ZContext;

public class Server
{
    public static long factorial(long n)
    {
        int i, result=1;  
        for(i=2; i<=n; i++) {    
            result *= i;
        }
        return result;
    }

    public static void main(String[] args) throws Exception
    {
        try (ZContext context = new ZContext()) {
            ZMQ.Socket socket = context.createSocket(ZMQ.REP);
            socket.bind("tcp://*:5555");

            while (!Thread.currentThread().isInterrupted()) {
                byte[] raw_request = socket.recv(0);
                String request = new String(raw_request, ZMQ.CHARSET);
                String response = null;

                System.out.println("Received: " + request);

                try {
                    long n = Integer.parseInt(request);
                    if (n < 0) {
                        response = "Invalid input!";
                    } else {
                        response = n + "! = " + Server.factorial(n);
                    }
                }
                catch (Exception e) {
                    response = "Wrong input!";
                }

                socket.send(response.getBytes(ZMQ.CHARSET), 0);
            }
        }
    }
}
