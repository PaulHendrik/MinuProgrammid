/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package personalcode;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author paul.maimik
 */
public class ReadCode {

    private String id;
    private boolean idValid;
    private boolean dateValid;
    private String strGender;
    private int intGender;
    private String strYear;
    private String strYearLong;
    private String strMonth;
    private int intMonth;
    private String wordMonth;
    private String strSmallMonth;
    private String strDay;
    private int intDay;
    private String strSmallDay;
    private String strHospital;
    private String strControlCode;
    private String strHospitalName;
    private String strCentury;
    String DATE_FORMAT = "dd.MM.yyyy";
    private final String[] monthNames = {"", "Jaanuar", "Veebruar", "Märts", "Aprill",
        "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"};
    List<Hospitals> hospitals = new ArrayList<>();

    ;

    ReadCode(String id) {
        if (id.matches("\\d+") && id.length() == 11 && checkLastNumber(id)) {
            this.idValid = true;
            this.id = id;
            if (isThisDateCorrect(id)) {
                this.strGender = this.id.substring(0, 1);
                this.strYear = this.id.substring(1, 3);
                this.strYearLong = getCentury() + this.id.substring(1, 3);
                this.strMonth = this.id.substring(3, 5);
                this.strDay = this.id.substring(5, 7);
                this.strHospital = this.id.substring(7, 10);
                this.strControlCode = this.id.substring(10, 11);
                setHospital();
                this.strHospitalName = getHospitalName();
                this.wordMonth = monthNames[intMonth];
            } else {
                idValid = false;
            }
        } else {
            this.idValid = false;
        }
    }

    private boolean checkLastNumber(String id) {
        String[] parts = id.split("(?!^)");
        boolean result = false;
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
        if (Integer.parseInt(parts[10]) == modula) {
            result = true;
        }
        return result;
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

    private String getDate() {
        String date;
        intMonth = Integer.parseInt(id.substring(3, 5));
        intDay = Integer.parseInt(id.substring(5, 7));
        strYearLong = getCentury() + id.substring(1, 3);
        if (intMonth < 10) {
            strSmallMonth = String.format("%02d", intMonth);
        } else {
            strSmallMonth = String.valueOf(intMonth);
        }
        if (intDay < 10) {
            strSmallDay = String.format("%02d", intDay);
        } else {
            strSmallDay = String.valueOf(intDay);
        }
        date = strSmallDay + "." + strSmallMonth + "." + strYearLong;
        dateValid = isDateValid(date);
        return date;
    }

    private String getCentury() {
        intGender = Integer.parseInt(id.substring(0, 1));
        switch (intGender) {
            case 1:
            case 2:
                strCentury = "18";
                break;
            case 3:
            case 4:
                strCentury = "19";
                break;
            case 5:
            case 6:
                strCentury = "20";
                break;
            case 7:
            case 8:
                strCentury = "21";
                break;
            default:
                break;
        }
        return strCentury;
    }

    private boolean isThisDateCorrect(String id) {
        intGender = Integer.parseInt(id.substring(0, 1));
        String date = getDate();
        return isDateValid(date);
    }

    private String getHospitalName() {
        int hospitalCode = Integer.parseInt(strHospital);
        String hospitalName = "Välismaalane";
        for (int i = 0; i < hospitals.size(); i++) {
            String code = hospitals.get(i).getHospitalCode();
            String[] twoCodes = code.split("-");
            int startCode = Integer.parseInt(twoCodes[0]);
            int endCode = Integer.parseInt(twoCodes[1]);
            if (hospitalCode >= startCode && hospitalCode <= endCode) {
                hospitalName = hospitals.get(i).getHospitalName();
                break;
            }
        }
        return hospitalName;
    }

    private void setHospital() {
        hospitals.add(new Hospitals("001-010", "Kuressaare Haigla"));
        hospitals.add(new Hospitals("011-019", "Tartu Ülikooli Naistekliinik, \nTartumaa, Tartu"));
        hospitals.add(new Hospitals("021-220", "Ida-Tallinna Keskhaigla, \nPelgulinna sünnitusmaja, \nHiiumaa, Keila, \nRapla haigla, \nLoksa haigla"));
        hospitals.add(new Hospitals("221-270", "Ida-Viru Keskhaigla"));
        hospitals.add(new Hospitals("271-370", "Maarjamõisa Kliinikum, \nJõgeva Haigla"));
        hospitals.add(new Hospitals("371-420", "Narva Haigla"));
        hospitals.add(new Hospitals("421-470", "Pärnu Haigla"));
        hospitals.add(new Hospitals("471-490", "Pelgulinna Sünnitusmaja, \nHaapsalu haigla"));
        hospitals.add(new Hospitals("491-520", "Järvamaa Haigla"));
        hospitals.add(new Hospitals("521-570", "Rakvere, \nTapa haigla"));
        hospitals.add(new Hospitals("571-600", "Valga Haigla"));
        hospitals.add(new Hospitals("601-650", "Viljandi Haigla"));
        hospitals.add(new Hospitals("651-710", "Lõuna-Eesti Haigla, \nPõlva Haigla"));
    }

    public long getAge() {
        LocalDate end = LocalDate.now();
        LocalDate start = LocalDate.of(Integer.parseInt(strYearLong), Integer.parseInt(strMonth), Integer.parseInt(strDay));
        long age = ChronoUnit.YEARS.between(start, end);
        if (age < 0) {
            age = -1;
        }
        return age;
    }

    public String getStrGender(int shortLong) {
        if ((intGender % 2) == 0) {
            if (shortLong == 0) {
                strGender = "N";
            } else if (shortLong == 1) {
                strGender = "Naine";
            }
        } else if (shortLong == 0) {
            strGender = "M";
        } else if (shortLong == 1) {
            strGender = "Mees";
        }
        return strGender;
    }

    public int getIntGender() {
        return intGender;
    }

    public int getShortOrLongYear(int shortLong) {
        int year = 0;
        if (shortLong == 0) {
            year = Integer.parseInt(strYear);
        } else if (shortLong == 1) {
            year = Integer.parseInt(strYearLong);
        }
        return year;
    }

    public int getIntBirthMonth() {
        return intMonth;
    }

    public String getStrBirthMonth() {
        return wordMonth;
    }

    public int getIntBirthDay() {
        return intDay;
    }

    public String getFullBirthDate() {
        String date = strSmallDay + "." + strSmallMonth + "." + strYearLong;
        return date;
    }

    public int getIntHospitalCode() {
        return Integer.parseInt(strHospital);
    }

    public String getStrHospitalCode() {
        return strHospitalName;
    }

    public int getControlCode() {
        return Integer.parseInt(strControlCode);
    }

    public boolean isValid() {
        return idValid;
    }

}
