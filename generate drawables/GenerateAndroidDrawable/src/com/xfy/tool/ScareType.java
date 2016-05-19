package com.xfy.tool;

/**
 * Created by XK on 16/1/15.
 */
public enum ScareType {

    XXXHDPI("xxxhdpi",4f),
    XXHDPI("xxhdpi",3f),
    XHDPI("xhdpi",2f),
    HDPI("hdpi",1.5f),
    MDPI("mdpi",1f),
    LDPI("ldpi",0.75f);

    private String str;

    private float scale;

    ScareType(String string,float f){
        str = string;
        scale = f;
    }

    public String toString(){
        return str;
    }

    public float getScale(){
        return scale;
    }
}
