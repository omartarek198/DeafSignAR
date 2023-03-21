using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Windows.Forms;
using System.Net.Sockets;
using socketApp;


namespace socketApp
{
    public partial class Form1 : Form
    {
        public int byteCount;
        public NetworkStream stream;
        public byte[] data2send;
        public TcpClient tcpClient;
        public string text ="";

        public System.Windows.Forms.Timer tt = new System.Windows.Forms.Timer();

        public Bitmap off;


        public bool connectToSocket(String host, int portNumber)
        {
            try
            {
                tcpClient = new TcpClient(host, portNumber);
                stream = tcpClient.GetStream();
                Console.WriteLine("Connection Made ! with " + host);
                return true;
            }
            catch (System.Net.Sockets.SocketException e)
            {
                Console.WriteLine("Connection Failed: " + e);
                return false;
            }
        }

        public bool recieveMessage()
        {
            try
            {
                // Receive some data from the peer.
                byte[] receiveBuffer = new byte[1024];
                int bytesReceived = stream.Read(receiveBuffer);
                string data = Encoding.UTF8.GetString(receiveBuffer.AsSpan(0, bytesReceived));
                //points = data.Split(",");
                text = data;
                Console.WriteLine(text);
                return true;


            }
            catch (Exception e)
            {
                Console.WriteLine("Connection not initialized : " + e);
                return false;
            }
        }

        public bool closeConnection()
        {
            stream.Close();
            tcpClient.Close();
            Console.WriteLine("Connection terminated ");
            return true;
        }

        public int cnvrtX(string x)
        {
            float s = float.Parse(x);
            int tb = (1800 * ((int)s) / 600);
            return tb;
        }

        public int cnvrtY(string y)
        {
            float s = float.Parse(y);
            int tb = (980 * ((int)s / 450));

            return tb;
        }

        public Form1()
        {

            this.WindowState = FormWindowState.Maximized;
            this.Load += Form1_Load;
            tt.Tick += Tt_Tick;
            tt.Start();
            this.Paint += Form1_Paint;
        }

        private void Form1_Paint(object? sender, PaintEventArgs e)
        {
            drawd(CreateGraphics());
        }

        private void Form1_Load(object? sender, EventArgs e)
        {
            connectToSocket("localhost", 5000);

            off = new Bitmap(ClientSize.Width, ClientSize.Height);
            try
            {
                recieveMessage();
            }
            catch
            {

            }
            drawd(CreateGraphics());

        }

        private void Tt_Tick(object? sender, EventArgs e)
        {
            
            drawd(CreateGraphics());
        }

        public void draw(Graphics g)
        {
            g.Clear(Color.White);
            g.DrawString(text, new Font(FontFamily.GenericSansSerif, 30), Brushes.Black, new PointF(ClientSize.Width / 2, ClientSize.Height / 2));
        }
        public void drawd(Graphics g)
        {
            Graphics g2 = Graphics.FromImage(off);
            draw(g2);
            g.DrawImage(off,0,0);
        }
    }
}