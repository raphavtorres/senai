public abstract class Patient {
    protected String name;
    protected float weight;
    protected int age;
    protected String gender;
    protected boolean isSick;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getWeight(){
        return this.weight;
    }
    public void setWeight(float weight){
        this.weight = weight;
    }
    public int getAge(){
        return age;
    }
    public void setAge(int age){
        this.age = age;
    }
    public String getGender(){
        return gender;
    }
    public void setGender(String gender){
        this.gender = gender;
    }
    public boolean getIsSick(){
        return isSick;
    }
    public void setSick(boolean isSick){
        this.isSick = isSick;
    }

    public abstract void changeWeight();
    public abstract void takeMedicine();
    public abstract void getSick();
    public abstract void getOlder();
}
