public class OldPatient extends Patient{

    private String retirement;
    public OldPatient(String retirement){
        this.retirement = retirement;
    }
    public String getRetirement(){
        return retirement;
    }
    public void setRetirement(String retirement) {
        this.retirement = retirement;
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
