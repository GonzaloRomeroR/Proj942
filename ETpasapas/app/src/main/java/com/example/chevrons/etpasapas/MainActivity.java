package com.example.chevrons.etpasapas;

import android.content.ContentValues;
import android.content.Intent;
import android.hardware.Camera;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;



import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.SimpleDateFormat;
import java.util.Date;

import java.io.FileNotFoundException;
import java.io.InputStream;

public class MainActivity extends AppCompatActivity implements SurfaceHolder.Callback{

    //Attribut
    private Button bt_selection_image;
    private Button bt_prendre_photo;
    private Button bt_envoie_image;
    private Camera camera;
    private SurfaceView surfaceCamera;
    private Boolean isPreview;
    private FileOutputStream stream;
    static final int RESULT_LOAD_IMG = 1;
    private ImageView selectImage;
    private Bitmap selectedImage;
    private Uri imageUri;
    private OutputStream stream_envoie;
    private SeekBar scroll;

    @Override
    protected void onCreate(Bundle savedInstanceState) {    //Creation de la fen
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main); //set visible

        //relie l'interface graphique & les variables
        bt_selection_image = (Button) findViewById(R.id.button);
        bt_prendre_photo = (Button) findViewById(R.id.button2);
        bt_envoie_image = (Button) findViewById(R.id.button3);
        selectImage = (ImageView) findViewById(R.id.imageView2);
        scroll = (SeekBar) findViewById(R.id.seekBar);

        //helloWorld = (TextView) findViewById(R.id.txtHelloWorld);


        bt_selection_image.setOnClickListener(new View.OnClickListener(){ //listener bouton 1
            public void onClick(View v) {
                    Intent photoPickerIntent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                    photoPickerIntent.setType("image/*");
                    startActivityForResult(photoPickerIntent, RESULT_LOAD_IMG);

            }
        });

        bt_envoie_image.setOnClickListener(new View.OnClickListener(){ // bouton envoie
            public void onClick(View v) {
                envoie_image();

            }
        });



        bt_prendre_photo.setOnClickListener(new View.OnClickListener() { //lsitener bouton 2, prendre une photo
            public void onClick(View v) {
                if (camera != null){
                    SavePicture();
                }
            }
        });

        //Gestion camera
        isPreview = false;
        surfaceCamera = (SurfaceView) findViewById(R.id.surfaceView);
        InitializeCamera();
}



    public void InitializeCamera(){
        surfaceCamera.getHolder().addCallback(this);
        surfaceCamera.getHolder().setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);

    }
    public void surfaceChanged(SurfaceHolder holder, int format, int width,int height) {
        if (isPreview) {
            camera.stopPreview();
        }
        Camera.Parameters parameters = camera.getParameters();

        camera.setDisplayOrientation(90);
        //camera.setZoomChangeListener();
        parameters.setPreviewSize(width, height);
        //camera.setParameters(parameters);

        try {
            camera.setPreviewDisplay(surfaceCamera.getHolder());
        } catch (IOException e) {
            e.printStackTrace();
        }
        camera.startPreview();
        isPreview = true;
    }


    public void surfaceCreated(SurfaceHolder holder){ //creation camera
        if (camera == null){
            camera = Camera.open();
        }
    }

    public void surfaceDestroyed(SurfaceHolder holder){ //arrêt camera
        if (camera != null){
            camera.stopPreview();
            isPreview = false;
            camera.release();
        }
    }

    private void SavePicture(){
        try{
            SimpleDateFormat timeStampFormat = new SimpleDateFormat(
                    "yyyy-MM-dd-HH.mm.ss");
            String fileName = "photo_" + timeStampFormat.format(new Date())
                    + ".jpg";

            // Metadata pour la photo
            ContentValues values = new ContentValues();
            values.put(MediaStore.Images.Media.TITLE, fileName);
            values.put(MediaStore.Images.Media.DISPLAY_NAME, fileName);
            values.put(MediaStore.Images.Media.DESCRIPTION, "Image prise par FormationCamera");
            values.put(MediaStore.Images.Media.DATE_TAKEN, new Date().getTime());
            values.put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg");

            // Support de stockage
            Uri taken = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
                    values);

            // Ouverture du flux pour la sauvegarde
            stream = (FileOutputStream) getContentResolver().openOutputStream(taken);

            camera.takePicture(null, pictureCallback, pictureCallback);
        } catch (Exception e) {
            e.printStackTrace();
        };
        }

        Camera.PictureCallback pictureCallback = new Camera.PictureCallback() {
            @Override
            public void onPictureTaken(byte[] data, Camera camera) {
                if (data != null){
                    try {
                        if (stream != null) {
                            stream.write(data);
                            stream.flush();
                            stream.close();
                        }
                        } catch (Exception e){
                            e.printStackTrace();
                        }
                        camera.startPreview();
                    }
                }
    };


    public void onResume() {
        super.onResume();
        camera = Camera.open();

    }

    // Mise en pause de l'application
    @Override
    public void onPause() {
        super.onPause();

        if (camera != null) {
            camera.release();
            camera = null;
        }
    }


    protected void onActivityResult(int reqCode, int resultCode, Intent data){
        super.onActivityResult(reqCode, resultCode, data);

        if (resultCode == RESULT_OK) {

            imageUri = data.getData();
            try {
                selectedImage = MediaStore.Images.Media.getBitmap(getContentResolver(),imageUri);

                selectImage.setImageBitmap(selectedImage);
            } catch (IOException e) {
                e.printStackTrace();
                Toast.makeText(getApplicationContext(), "Une erreur s'est produite",Toast.LENGTH_LONG).show();

            }

        }else {
            Toast.makeText(getApplicationContext(),"Vous n'avez pas choisi d'image", Toast.LENGTH_LONG).show();

        }
    }

    private void envoie_image() {
        //test co
        //stream_envoie = new FileOutputStream(new File(imageUri))
    }

    private void connexion() {

    }
}


