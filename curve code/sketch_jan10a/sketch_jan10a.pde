noFill();
color(255,255,255);

int[] x_s = {1000, 3000, 1000, 2100};
int[] y_s = {1000, 1500, 2500, 3000};
int[] i_x = {1500, 2000, 1500, 700};
int[] i_y = {1000, 2000, 2700, 1700};
//int[] i_x = {2500-1000, 2500-500, 2500+500, 2500+1000};
//int[] i_y = {2500-1000, 2500+500, 2500-500, 2500+1000};

fill(255);
size(4096/5,4096/5);
int steps = 300;

for (int step = 0; step <= steps; step++) {
  float t = step / float(steps);

  
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      for(int k = 0; k < 4; k++)
        for(int l = 0; l < 4; l++)
          {
            if(i != l){
              float x = bezierPoint(x_s[i], i_x[j], i_x[k], x_s[l], t);
              float y = bezierPoint(y_s[i], i_y[j], i_y[k], y_s[l], t);
              ellipse(x/5, y/5, 0.1, 0.1);
              print((int)x + " " + (int)y + "\n");
            }
          }
  
}

