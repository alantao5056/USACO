/*
ID: alantao
LANG: JAVA
TASK: castle
*/

import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;


class castle {
  static class Coords {
    int i, j;
    Coords (int i, int j) {
      this.i = i;
      this.j = j;
    }
  }
  static class Wall {
    Coords coord;
    int id;
    int direction;
    int removeValue = -1;

    Wall (Coords coord, int direction, int id) {
      this.coord = coord;
      this.direction = direction;
      this.id = id;
    }
  }
  static class Room {
    Room left, right, up, down;
    int id, x;
    Coords coord;

    boolean leftWall = false;
    boolean rightWall = false;
    boolean upWall = false;
    boolean downWall = false;

    Wall leftWallClass = null;
    Wall rightWallClass = null;
    Wall upWallClass = null;
    Wall downWallClass = null;

    Room (int x, int id, Coords coord) {
      this.id = id;
      this.coord = coord;
      this.x = x;
    }

    void generateWalls() {
      // generate room
      if (this.x == 0) {
        // no wall
      } else if (this.x == 1) {
        // left wall
        makeLeftWall();
      } else if (this.x == 2) {
        // up wall
        makeUpWall();
      } else if (this.x == 3) {
        // left wall, up wall
        makeLeftWall();
        makeUpWall();
      } else if (this.x == 4) {
        // right wall
        makeRightWall();
      } else if (this.x == 5) {
        // right wall, left wall
        makeRightWall();
        makeLeftWall();
      } else if (this.x == 6) {
        // up wall, right wall
        makeUpWall();
        makeRightWall();
      } else if (this.x == 7) {
        // up wall, right wall, left wall
        makeUpWall();
        makeRightWall();
        makeLeftWall();
      } else if (this.x == 8) {
        // down wall
        makeDownWall();
      } else if (this.x == 9) {
        // left wall, down wall
        makeLeftWall();
        makeDownWall();
      } else if (this.x == 10) {
        // up wall, down wall
        makeUpWall();
        makeDownWall();
      } else if (this.x == 11) {
        // left wall, up wall, down wall
        makeLeftWall();
        makeUpWall();
        makeDownWall();
      } else if (this.x == 12) {
        // right wall, down wall
        makeRightWall();
        makeDownWall();
      } else if (this.x == 13) {
        // right wall, down wall, left wall
        makeRightWall();
        makeDownWall();
        makeLeftWall();
      } else if (this.x == 14) {
        // up wall, right wall, down wall
        makeUpWall();
        makeRightWall();
        makeDownWall();
      } else {
        // up wall, right wall, down wall, left wall
        makeUpWall();
        makeRightWall();
        makeDownWall();
        makeLeftWall();
      }
    }

    void makeUpWall() {
      if (this.up != null) {
        upWallClass = new Wall(this.coord, 1, this.up.id);
      }
      this.upWall = true;
    }

    void makeDownWall() {
      if (this.down != null) {
        downWallClass = new Wall(this.coord, 2, this.down.id);
      }
      this.downWall = true;
    }
    void makeLeftWall() {
      if (this.left != null) {
        leftWallClass = new Wall(this.coord, 3, this.left.id);
      }
      this.leftWall = true;
    }
    void makeRightWall() {
      if (this.right != null) {
        rightWallClass = new Wall(this.coord, 4, this.right.id);
      }
      this.rightWall = true;
    }
  }

  static int M;
  static int N;
  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("castle.in")));
    StringTokenizer st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("castle.out"));

    final int N = Integer.parseInt(st.nextToken());
    final int M = Integer.parseInt(st.nextToken());

    Room[][] castle = new Room[M + 2][N + 2];
    Room[] flatCastle = new Room[M*N + 1];

    // filling with rooms
    int curRoom;
    int id;
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        curRoom = Integer.parseInt(st.nextToken());
        id = (i - 1)*N + j;
        castle[i][j] = new Room(curRoom, id, new Coords(i, j));
        flatCastle[id] = castle[i][j];
      }
    }

    // linking rooms
    Room room;
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        room = castle[i][j];
        room.up = castle[i - 1][j];
        room.down = castle[i + 1][j];
        room.left = castle[i][j - 1];
        room.right = castle[i][j + 1];
      }
    }

    // generating walls
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        castle[i][j].generateWalls();
      }
    }

    // flood fill rooms to get num of rooms
    // and largest room
    boolean[] visited = new boolean[N*M + 1];
    int[] roomGroupSize = new int[N*M + 1];
    int[] roomGroupId = new int[N*M + 1];
    int numOfRooms = 0;
    int maxRoomSize = 0;
    int maxRoomSizeId = -1;
    int maxRoomGroupId = 0;

    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        Room roomToSearch = castle[i][j];
        List<Integer> group = new ArrayList<>();
        int thisRoomSize = 0;

        if (roomToSearch != null && !visited[roomToSearch.id]) {
          // need to be searched
          numOfRooms++;
          Queue<Integer> q = new LinkedList<>();
          q.add(roomToSearch.id);
          
          while (!q.isEmpty()) {
            int curRoomId = q.poll();
            Room myRoom = flatCastle[curRoomId];
            if (!visited[myRoom.id]) {
              thisRoomSize++;
              visited[curRoomId] = true;
              group.add(curRoomId);

              if (!myRoom.upWall && myRoom.up != null && !visited[myRoom.up.id]) {
                q.add(myRoom.up.id);
              }
              if (!myRoom.rightWall && myRoom.right != null && !visited[myRoom.right.id]) {
                q.add(myRoom.right.id);
              }
              if (!myRoom.downWall && myRoom.down != null && !visited[myRoom.down.id]) {
                q.add(myRoom.down.id);
              }
              if (!myRoom.leftWall && myRoom.left != null && !visited[myRoom.left.id]) {
                q.add(myRoom.left.id);
              }
            }
          }

          if (thisRoomSize > maxRoomSize) {
            maxRoomSize = thisRoomSize;
            maxRoomSizeId = roomToSearch.id;
            maxRoomGroupId = numOfRooms + 1;
          }

          for (int g : group) {
            roomGroupSize[g] = thisRoomSize;
            roomGroupId[g] = numOfRooms + 1;
          }
        }
      }
    }

    pw.println(numOfRooms);
    pw.println(maxRoomSize);


    // find the max room size connected to max rooms
    int maxTwoId = 0;
    List<Wall> possibleWalls = new ArrayList<>();
    
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        Room myRoom = castle[i][j];
        int curRoomId = myRoom.id;
        int curRoomSize = roomGroupSize[myRoom.id];
        int removeValue;

        if (myRoom.up != null && myRoom.upWall) {
          if (roomGroupId[myRoom.up.id] == roomGroupId[curRoomId]) {
            // this wall connects the same two rooms
            removeValue = curRoomSize;
            maxTwoId = Math.max(maxTwoId, curRoomSize);
          } else {
            // this wall ok
            removeValue = curRoomSize + roomGroupSize[myRoom.up.id];
            maxTwoId = Math.max(maxTwoId, removeValue);
          }
          myRoom.upWallClass.removeValue = removeValue;
          possibleWalls.add(myRoom.upWallClass);
        }

        if (myRoom.down != null && myRoom.downWall) {
          if (roomGroupId[myRoom.down.id] == roomGroupId[curRoomId]) {
            // this wall connects the same two rooms
            removeValue = curRoomSize;
            maxTwoId = Math.max(maxTwoId, curRoomSize);
          } else {
            // this wall ok
            removeValue = curRoomSize + roomGroupSize[myRoom.down.id];
            maxTwoId = Math.max(maxTwoId, removeValue);
          }
          myRoom.downWallClass.removeValue = removeValue;
          possibleWalls.add(myRoom.downWallClass);
        }

        if (myRoom.left != null && myRoom.leftWall) {
          if (roomGroupId[myRoom.left.id] == roomGroupId[curRoomId]) {
            // this wall connects the same two rooms
            removeValue = curRoomSize;
            maxTwoId = Math.max(maxTwoId, curRoomSize);
          } else {
            // this wall ok
            removeValue = curRoomSize + roomGroupSize[myRoom.left.id];
            maxTwoId = Math.max(maxTwoId, removeValue);
          }
          myRoom.leftWallClass.removeValue = removeValue;
          possibleWalls.add(myRoom.leftWallClass);
        }
        
        if (myRoom.right != null && myRoom.rightWall) {
          if (roomGroupId[myRoom.right.id] == roomGroupId[curRoomId]) {
            // this wall connects the same two rooms
            removeValue = curRoomSize;
            maxTwoId = Math.max(maxTwoId, curRoomSize);
          } else {
            // this wall ok
            removeValue = curRoomSize + roomGroupSize[myRoom.right.id];
            maxTwoId = Math.max(maxTwoId, removeValue);
          }
          myRoom.rightWallClass.removeValue = removeValue;
          possibleWalls.add(myRoom.rightWallClass);
        }
      }
    }

    pw.println(maxTwoId);

    List<Wall> maxRoomWalls = new ArrayList<>();
    for (Wall p : possibleWalls) {
      if (p.removeValue == maxTwoId) {
        maxRoomWalls.add(p);
      }
    }

    // modify list so direction is only north / east
    for (int i = 0; i < maxRoomWalls.size(); i++) {
      Wall w = maxRoomWalls.get(i);
      if (w.direction == 2) {
        // facing south
        maxRoomWalls.set(i, new Wall(new Coords(w.coord.i - 1, w.coord.j), 1, -1));
      } else if (w.direction == 3) {
        // facing south
        maxRoomWalls.set(i, new Wall(new Coords(w.coord.i, w.coord.j - 1), 4, -1));
      }
    }

    // sort using problem restrictions
    Collections.sort(maxRoomWalls, new Comparator<Wall>(){
      @Override
      public int compare(final Wall a,Wall b) {
        // return 1 if a should be before b 
        // return -1 b lhs should be before a
        // return 0 otherwise (meaning the order stays the same)
        if (a.coord.j < b.coord.j) {
          return -1;
        } else if (a.coord.j > b.coord.j) {
          return 1;
        } else {
          // the j's are the same
          if (a.coord.i > b.coord.i) {
            return -1;
          } else if (a.coord.i < b.coord.i) {
            return 1;
          } else {
            // the i's are the same
            // they are in the same room
            if (a.direction == 1) {
              // facing north or south
              return -1;
            } else {
              return 1;
            }
          }
        }
      }
    });

    // found result, final modification
    Wall result = maxRoomWalls.get(0);
    if (result.direction == 2) {
      // facing south
      pw.printf("%d %d %c\n", result.coord.i + 1, result.coord.j, 'N');
    } else if (result.direction == 3 ) {
      // facing west
      pw.printf("%d %d %c\n", result.coord.i, result.coord.j - 1, 'E');
    } else {
      pw.printf("%d %d ", result.coord.i, result.coord.j);

      if (result.direction == 1) {
        // north
        pw.printf("%c\n", 'N');
      } else {
        pw.printf("%c\n", 'E');
      }
    }

    pw.close();
  }
}