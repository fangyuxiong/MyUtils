package com.xfy.tool;

import javax.imageio.ImageIO;
import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

/**
 * Created by XK on 16/1/15.
 */
public class ImageScaleUtil {

    private File srcFile;

    private float srcScale;

    private Image srcImg;

    private int width,height;

    public ImageScaleUtil(File imageFile){
        this(imageFile,ScareType.XXHDPI);
    }

    public ImageScaleUtil(File imageFile, ScareType type){
        srcFile = imageFile;
        this.srcScale = type.getScale();
        init();
    }

    private void init(){
        try {
            srcImg  = ImageIO.read(new FileInputStream(srcFile));
            width = srcImg.getWidth(null);
            height = srcImg.getHeight(null);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Image generateImage(ScareType type){
        float scale = type.getScale();
        if (scale < srcScale){
            int outW = (int) (width * scale / srcScale);
            int outH = (int) (height * scale / srcScale);
            return srcImg.getScaledInstance(outW,outH,Image.SCALE_SMOOTH);
        }else if (scale == srcScale)
            return srcImg;
        else
            return srcImg;
    }
}
