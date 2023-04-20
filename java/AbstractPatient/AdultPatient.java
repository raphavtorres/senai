public class AdultPatient extends Patient{
    private String work;
    public AdultPatient(String work){
        this.work = work;
    }

    public String getWork() {
        return work;
    }

    public void setWork(String work) {
        this.work = work;
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
