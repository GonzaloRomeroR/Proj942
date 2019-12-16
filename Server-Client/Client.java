import java.io.*;
import java.net.*;
import java.nio.file.Files;
import java.util.Base64;
import java.util.concurrent.TimeUnit;


public class Client{


   private static String encodeFileToBase64Binary(File file){
        String encodedfile = null;
        try {
            FileInputStream fileInputStreamReader = new FileInputStream(file);
            byte[] bytes = new byte[(int)file.length()];
            fileInputStreamReader.read(bytes);
            encodedfile = Base64.getEncoder().encodeToString(bytes);
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return encodedfile;
    }

  public static void main(String[] args){

    try{

      // 
      String url = "http://10.7.177.93:4000";
      String charset = "UTF-8";
      File image = new File("hugo.jpg");
      String encodedstring = encodeFileToBase64Binary(image);
      //System.out.print(encodedstring);
      
      URLConnection connection = new URL(url).openConnection();
      connection.setDoOutput(true);
      
      OutputStream output = connection.getOutputStream();
      PrintWriter writer = new PrintWriter(new OutputStreamWriter(output, charset), true);
      
      System.out.println(encodedstring.length());

      writer.append(encodedstring);
      
      output.flush(); 
      writer.flush();
      //TimeUnit.SECONDS.sleep(1);
      try{
        int responseCode = ((HttpURLConnection) connection).getResponseCode();
        System.out.println(responseCode);
      }
      catch(Exception e){
        e.printStackTrace();
  
      }

      

    }catch(Exception e){
      
      e.printStackTrace();
    }

  }
}
