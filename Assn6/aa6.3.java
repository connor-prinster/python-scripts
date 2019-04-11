import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class QuestionTres {
    public static void main(String[] args) {
        Vertex s, a, b, c, e, g, t;
        s = new Vertex("s");
        a = new Vertex("a");
        b = new Vertex("b");
        c = new Vertex("c");
        e = new Vertex("e");
        g = new Vertex("g");
        t = new Vertex("t");

        ArrayList<Vertex> outS = new ArrayList();
        outS.add(e);
        outS.add(c);
        s.addAdj(outS);
        ArrayList<Vertex> outA = new ArrayList();
        outA.add(b);
        outA.add(c);
        a.addAdj(outA);
        ArrayList<Vertex> outB = new ArrayList();
        outB.add(c);
        outB.add(g);
        b.addAdj(outB);
        ArrayList<Vertex> outC = new ArrayList<>();
        outC.add(t);
        c.addAdj(outC);
        ArrayList<Vertex> outE = new ArrayList<>();
        outE.add(c);
        e.addAdj(outE);
        ArrayList<Vertex> outG = new ArrayList<>();
        outG.add(t);
        g.addAdj(outG);

        t.addAdj(null);
        ArrayList<Vertex> vertices = new ArrayList<>();
        vertices.add(s);
        vertices.add(a);
        vertices.add(b);
        vertices.add(c);
        vertices.add(e);
        vertices.add(g);
        vertices.add(t);

        Queue<Vertex> queue = new LinkedList<>();

        for (Vertex v : vertices) {
            if (v.indegree == 0) queue.add(v);
        }
        HashMap<String, Integer> paths = new HashMap<>();
        for (Vertex v : vertices) {
            if (v.id.equals("s")) paths.put("s", 1);
            else paths.put(v.id, 0);
        }

        while (queue.size() != 0) {
            Vertex u = queue.remove();
            for (Vertex v : u.outVertices) {
                v.indegree--;
                paths.put(v.id, paths.get(v.id) + paths.get(u.id));
                if (v.indegree == 0) queue.add(v);
            }
        }
        System.out.println("Paths from s to t: " + paths.get(t.id));
    }
}

class Vertex {
    public String id;
    public int indegree = 0;
    public ArrayList<Vertex> outVertices = new ArrayList();

    public Vertex(String id) {
        this.id = id;
    }

    public void addAdj(ArrayList<Vertex> outVerts) {
        if (outVerts != null) {
            for (int i = 0; i < outVerts.size(); i++) {
                outVertices.add(outVerts.get(i));
                outVerts.get(i).indegree++;
            }
        }
    }
}
