ArrayList<PVector> allPoints = new ArrayList<PVector>();
float epsilon = 0;
float epsilonMax = 100;

void setup() {
  fullScreen();
  //size(600, 400);
  //surface.setLocation(1200, 100);

  for (int x = 0; x < width; x++) {
    float xval = map(x, 0, width, 0, 5);
    float yval = exp(-xval) * cos(TWO_PI * xval);
    float y = map(yval, -1, 1, height, 0);
    allPoints.add(new PVector(x, y));
  }


}

void rdp(int startIndex, int endIndex, ArrayList<PVector> allPoints, ArrayList<PVector> rdpPoints) {
  int nextIndex = findFurthest(allPoints, startIndex, endIndex);
  if (nextIndex > 0) {
    if (startIndex != nextIndex) {
      rdp(startIndex, nextIndex, allPoints, rdpPoints);
    }
    rdpPoints.add(allPoints.get(nextIndex));
    if (endIndex != nextIndex) {
      rdp(nextIndex, endIndex, allPoints, rdpPoints);
    }
  }
}
float lineDist(PVector c, PVector a, PVector b) {
  PVector norm = scalarProjection(c, a, b);
  return PVector.dist(c, norm);
}

PVector scalarProjection(PVector p, PVector a, PVector b) {
  PVector ap = PVector.sub(p, a);
  PVector ab = PVector.sub(b, a);
  ab.normalize();
  ab.mult(ap.dot(ab));
  PVector normalPoint = PVector.add(a, ab);
  return normalPoint;
}


int findFurthest(ArrayList<PVector> points, int a, int b) {
  float recordDistance = -1;
  PVector start = points.get(a);
  PVector end = points.get(b);
  int furthestIndex = -1;
  for (int i = a+1; i < b; i++) {
    PVector currentPoint = points.get(i);
    float d = lineDist(currentPoint, start, end);
    if ( d > recordDistance) {
      recordDistance = d;
      furthestIndex = i;
    }
  }
  if (recordDistance > epsilon) {
    return furthestIndex;
  } else {
    return -1;
  }
}


void draw() {
  background(0);
  ArrayList<PVector> rdpPoints = new ArrayList<PVector>();
  
  
  int total = allPoints.size();
  PVector start = allPoints.get(0);
  PVector end = allPoints.get(total-1);
  rdpPoints.add(start);
  rdp(0, total-1, allPoints, rdpPoints);
  rdpPoints.add(end);
  
  epsilon += 0.01;
  if (epsilon > epsilonMax) {
   epsilon = epsilonMax; 
  }
  
  
  
  stroke(255, 0, 255);
  strokeWeight(8);
  noFill();
  beginShape();
  for (PVector v : allPoints) {
    vertex(v.x, v.y);
  }
  endShape();


  stroke(255);
  strokeWeight(4);
  noFill();
  beginShape();
  for (PVector v : rdpPoints) {
    vertex(v.x, v.y);
    ellipse(v.x,v.y,8,8);
  }
  endShape();
  textSize(64);
  fill(255);
  text("n:" + rdpPoints.size(),width/8, height/8);
}
