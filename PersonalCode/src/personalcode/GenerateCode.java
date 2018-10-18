/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package personalcode;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Random;

/**
 *
 * @author paul.maimik
 */
public class GenerateCode {

    private final String DATE_FORMAT = "dd.MM.yyyy";
    private String date, strDay, strMonth, strYearShort;
    private String gender;
    private final boolean dataOk;
    public String code;

    public GenerateCode(String gender, String date) {
        if (checkGender(gender) && isDateValid(date)) {
            this.gender = gender;
            this.date = date;
            this.dataOk = true;
            this.strDay = date.split("\\.")[0];
            this.strMonth = date.split("\\.")[1];
            this.strYearShort = date.split("\\.")[2].substring(2);
        } else {
            this.dataOk = false;
        }
    }

    private boolean checkGender(String gender) {
        return gender.equalsIgnoreCase("M") || gender.equalsIgnoreCase("N");
    }

    private boolean isDateValid(String date) {
        try {
            DateFormat df = new SimpleDateFormat(DATE_FORMAT);
            df.setLenient(false);
            df.parse(date);
            return true;
        } catch (ParseException e) {
            return false;
        }
    }

    public boolean isValid() {
        return dataOk;
    }

    private String getCentury() {
        String year = date.split("\\.")[2]; // Aeg on 31.12.2000 => 2000
        return year.substring(0, 2);
    }

    private String setGender() {
        int centuryNr = Integer.parseInt(getCentury()); // Sajand on NR
        String result = "";
        switch (centuryNr) {
            case 18:
                if (gender.equalsIgnoreCase("M")) {
                    result = "1";
                } else {
                    result = "2";
                }
                break;
            case 19:
                if (gender.equalsIgnoreCase("M")) {
                    result = "3";
                } else {
                    result = "4";
                }
                break;
            case 20:
                if (gender.equalsIgnoreCase("M")) {
                    result = "5";
                } else {
                    result = "6";
                }
                break;
            case 21:
                if (gender.equalsIgnoreCase("M")) {
                    result = "7";
                } else {
                    result = "8";
                }
                break;
            default:
                result = "9";
                break;
        }
        return result;
    }

    public String genPersonalCode() {
        code = setGender() + strYearShort + strMonth + strDay + hospitalNr();
        code += genLastNumber();
        return code;
    }

    public int genLastNumber() {
        String[] parts = code.split("(?!^)");
        int[] firstTierNr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1};
        int[] secondTierNr = {3, 4, 5, 6, 7, 8, 9, 1, 2, 3};
        int total = 0;
        for (int i = 0; i < firstTierNr.length; i++) {
            total += firstTierNr[i] * Integer.parseInt(parts[i]);
        }
        int modula = total % 11;
        if (modula == 10) {
            total = 0;
            for (int i = 0; i < secondTierNr.length; i++) {
                total += (secondTierNr[i] * Integer.parseInt(parts[i]));
            }
            modula = total % 11;
        }
        return modula;
    }

    public String hospitalNr() {
        String hospitalNr = null;
        int hospital = randInt(1, 999);
        if (hospital < 100) {
            hospitalNr = String.format("%03d", hospital);
        } else if (hospital < 10) {
            hospitalNr = String.format("%04d", hospital);
        } else {
            hospitalNr = String.valueOf(hospital);
        }
        return hospitalNr;
    }

    private int randInt(int min, int max) {
        Random rand = new Random();
        int randomNum = rand.nextInt((max - min) + 1) + min;
        return randomNum;
    }

}
