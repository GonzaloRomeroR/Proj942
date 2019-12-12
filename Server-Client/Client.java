import java.io.*;
import java.net.*;
import java.nio.file.Files;
import java.util.Base64;
import java.util.concurrent.TimeUnit;


public class Client{


   private static String encodeFileToBase64Binary(File file){
    // Transformer le fichier a base64
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

      // Definir l'adresse du serveur
      String url = "http://10.7.177.93:4000";
      String charset = "UTF-8";
      // Trouver l'image
      File image = new File("imagen.jpeg");
      // Encode base64
      String encodedstring = encodeFileToBase64Binary(image);
      // Ouvrir connection
      URLConnection connection = new URL(url).openConnection();
      connection.setDoOutput(true);
      
      OutputStream output = connection.getOutputStream();

      // Creer objet pour l'ecriture
      PrintWriter writer = new PrintWriter(new OutputStreamWriter(output, charset), true);
      
      writer.append(encodedstring);
      
      output.flush(); 

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
