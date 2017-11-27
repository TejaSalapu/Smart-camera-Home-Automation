package com.androidsrc.client;

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
import android.widget.Button;

public class Client extends AsyncTask<Void, Integer, Void> {

	String dstAddress;
	int dstPort;
	String response="";
	byte[] b;
	//TextView textResponse;
	ImageView imageResponse;
	TextView textResponse;
	Bitmap bitmap;
	Button buttonDisplay;
	Client(String addr, int port,ImageView imageResponse,Button buttonDisplay) {
		dstAddress = addr;
		dstPort = port;
		this.imageResponse=imageResponse;
		this.buttonDisplay=buttonDisplay;
	}


	@Override
	protected Void doInBackground(Void... arg0) {

		Socket socket = null;

		try {
			socket = new Socket(dstAddress, dstPort);
			Log.d("soc","connected");

			Log.d("soc",socket.getLocalAddress().toString());

			ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
					1024);
			byte[] buffer = new byte[1024];

			int bytesRead;
			String check="1";

         /*
          * notice: inputStream.read() will block if no data return
          *
          */
			for(int i=1;i<=5;i++){
				InputStream inputStream = socket.getInputStream();
				while ((bytesRead = inputStream.read(buffer)) != -1) {
					byteArrayOutputStream.write(buffer, 0, bytesRead);
				}
				for(int j=0;j<buffer.length;j++){
					buffer[j]=0;
				}
				buffer = new byte[1024];
				b=byteArrayOutputStream.toByteArray();
				Log.d("buffer lenght - image",String.valueOf(b.length));
				Log.d("i val",String .valueOf(i));
				Log.d("path",Environment.DIRECTORY_PICTURES);
				String state;
				state=Environment.getExternalStorageState();
				Log.d("state",state);
				if(Environment.MEDIA_MOUNTED.equals(state))
				{
					File root= Environment.getExternalStorageDirectory();
					File dir=new File(root.getAbsolutePath()+"/MyappFile_New");
					Log.d("file path full",dir.getAbsolutePath());

					dir.mkdir();
					File file=new File(dir,"photo"+i+".jpg");
					FileOutputStream fileOutputStream=new FileOutputStream(file);
					fileOutputStream.write(b);
					fileOutputStream.close();

				}
				else {
					Log.d("state", "not eligible");
				}

				socket.close();
				Log.d("closed", "closed");
				inputStream.close();
				byteArrayOutputStream.flush();
				byteArrayOutputStream.reset();
				publishProgress((int) i);
				if(i!=5) {
					socket = new Socket(dstAddress, dstPort);
					Log.d("after soc call", "soc call a");
					InputStream inputStream1 = socket.getInputStream();
					Log.d("after inp str", "after inp str");
					bytesRead = inputStream1.read(buffer);
					Log.d("bytes read", String.valueOf(bytesRead));
					byteArrayOutputStream.write(buffer, 0, bytesRead);
					response += byteArrayOutputStream.toString("UTF-8");
					byteArrayOutputStream.flush();
					byteArrayOutputStream.reset();
					Log.d("response", response);

					for (int j = 0; j < buffer.length; j++) {
						buffer[j] = 0;
					}
					buffer = new byte[1024];
					Log.d("response", response);
					if (response.equals("1")) {
						response = "";
						Log.d("wait", "wait");
						while (true) {
							bytesRead = inputStream1.read(buffer);
							byteArrayOutputStream.write(buffer, 0, bytesRead);
							response += byteArrayOutputStream.toString("UTF-8");
							if (response.equals("0")) {
								response = "";
								byteArrayOutputStream.flush();
								byteArrayOutputStream.reset();
								socket.close();
								socket = new Socket(dstAddress, dstPort);
								break;
							}
						}
					}

				}
			}
         /*Log.d("b length",String.valueOf(b.length));
         bitmap = BitmapFactory.(b, 0, b.length);
         Log.d("bitmap length",String.valueOf(bitmap.getByteCount()));*/

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

	protected void onProgressUpdate(Integer... progress) {
		/**
		 * Sets current progress on ProgressDialog
		 */
		File root = Environment.getExternalStorageDirectory();
		File dir = new File(root.getAbsolutePath() + "/MyappFile_New");
		File file = new File(dir, "photo"+progress[0]+".jpg");
		try {
			FileInputStream fileInputStream = new FileInputStream(file);
            /*InputStreamReader inputStreamReader=new InputStreamReader(fileInputStream);
            BufferedReader bufferedReader=new BufferedReader(inputStreamReader);*/
			Bitmap bitmap = BitmapFactory.decodeStream(fileInputStream); //This gets the image

			fileInputStream.close();
			imageResponse.setImageBitmap(bitmap);
			imageResponse.setVisibility(View.VISIBLE);
			buttonDisplay.setVisibility(View.VISIBLE);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}


	@Override
	protected void onPostExecute(Void result) {

		//super.onPostExecute(result);


	}

}