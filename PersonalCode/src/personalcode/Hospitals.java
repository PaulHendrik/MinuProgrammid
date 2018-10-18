/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package personalcode;

/**
 *
 * @author paul.maimik
 */
public class Hospitals {

    String codes;
    String name;

    public Hospitals(String codes, String name) {
        this.codes = codes;
        this.name = name;
    }

    public String getHospitalCode() {
        return codes;
    }

    public String getHospitalName() {
        return name;
    }
}
