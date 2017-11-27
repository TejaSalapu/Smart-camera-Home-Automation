package com.androidsrc.client;


import android.graphics.Color;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * Created by bulaa on 10/31/2017.
 */

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.UnknownHostException;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import android.os.Environment;

public class status extends AsyncTask<Void, Void, Void> {

    String dstAddress;

    int dstPort;
    String response="";
    String response_modified;
    byte[] b;
    //TextView textResponse;
    TextView textResponse;
    String id="";

    status(String addr, int port,String id) {
        Log.d("con","yes");
        dstAddress = addr;
        dstPort = port;
        //this.textResponse=textResponse;
        this.id=id;
    }


    @Override
    protected Void doInBackground(Void... arg0) {

        Socket socket = null;

        try {
            socket = new Socket(dstAddress, dstPort);
            Log.d("soc upload","connected");

            Log.d("soc upload",socket.getLocalAddress().toString());

            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
                    1024);
            byte[] buffer = new byte[1024];

            OutputStream outputStream=socket.getOutputStream();

            DataOutputStream dataOutputStream=new DataOutputStream(outputStream);
            if(id.equals("cancelButton"))
            {
                dataOutputStream.write('0');
            }
            else{
                dataOutputStream.write('1');
            }

            dataOutputStream.flush();
            Log.d("data",String.valueOf(dataOutputStream));
            dataOutputStream.close();
        } catch (UnknownHostException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            //response = "UnknownHostException: " + e.toString();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            //response = "IOException: " + e.toString();
        } finally {
            if (socket != null) {
                try {
                    socket.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
        return null;
    }

    @Override
    protected void onPostExecute(Void result) {

        //super.onPostExecute(result);

        /*textResponse.setText(response_modified);
        textResponse.setTextColor(Color.BLACK);
        textResponse.setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
        textResponse.setTextSize(25);
        textResponse.setVisibility(View.VISIBLE);*/

    }

}
