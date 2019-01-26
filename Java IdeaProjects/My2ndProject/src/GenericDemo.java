interface Info{
    int getLevel();
}
class EmployeeInfo implements Info{
    public int rank;
    EmployeeInfo(int rank){this.rank = rank;}
    public int getLevel(){
        return this.rank;
    }
}
class Person<T extends Info>{
    public T info;
    Person(T info){
        this.info = info;
        info.getLevel();
    }
}
public class GenericDemo{
    public static void main(String[] args) {
        Person<EmployeeInfo> p1 = new Person<EmployeeInfo>(new EmployeeInfo(1));
    }
}








/*class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){this.rank = rank;}
}
class Person<T, S> {
    public T info;
    public S id;
    Person(T info, S id){
        this.info = info;
        this.id = id;
    }
    public <U> void printInfo(U info){
        System.out.println(info);
    }
}
public class GenericDemo{
    public static void main(String[] args) {
        EmployeeInfo e = new EmployeeInfo(1);
        Integer i = new Integer(10);
        Person p1 = new Person(e, i);
        p1.printInfo(e);
    }
}*/






/*
class EmployeeInfo {
    public int rank;
    EmployeeInfo(int rank){this.rank=rank;}
}
class Person<T, S> {
    public T info;
    public S id;
    Person(T info, S id){
        this.info = info;
        this.id = id;
    }
}
public class GenericDemo{
    public static void main(String[] args) {
        Integer id = new Integer(1);
        Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(new EmployeeInfo(1), id);
        System.out.println(p1.id.intValue());
    }
}



class Studentinfo{
    public int grade;
    Studentinfo(int grade){this.grade = grade;}
}
class StudentPerson{
    public Studentinfo info;
    StudentPerson(Studentinfo info) {this. info = info;}
}
class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){this.rank = rank;}
}
class EmployeePerson{
    public EmployeeInfo info;
    EmployeePerson(EmployeeInfo info) {this.info = info;}
}
public class GenericDemo {
    public static void main(String[] args) {
        Studentinfo si = new Studentinfo(2);
        StudentPerson sp = new StudentPerson(si);
        System.out.println(sp.info.grade); 2
        EmployeeInfo ei = new EmployeeInfo(1);
        EmployeePerson ep = new EmployeePerson(ei);
        System.out.println(ep.info.rank); 1
    }
}
*/

