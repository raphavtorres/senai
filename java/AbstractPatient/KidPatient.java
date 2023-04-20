public class KidPatient extends Patient {
    private String school;

    public KidPatient(String school) {
        this.school = school;
    }

    public String getSchool(){
        return school;
    }
    public void setSchool(String school){
        this.school = school;
    }

    @Override
    public void changeWeight() {

    }

    @Override
    public void takeMedicine() {

    }

    @Override
    public void getSick() {

    }

    @Override
    public void getOlder() {

    }
}
