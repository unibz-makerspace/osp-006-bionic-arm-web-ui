//#define ZMQ_STATIC

#include <zmq.h>
#include <stdio.h>

int main() {
  void * context = zmq_ctx_new();
  void * socket = zmq_socket(context, ZMQ_SUB);
  const char * prefix = "hand";
  printf("%d\n", sizeof(prefix));
  zmq_setsockopt(socket, ZMQ_SUBSCRIBE, prefix, sizeof(prefix));
  zmq_connect(socket, "tcp://127.0.0.1:5680");
  while(true) {
    char message[32] = { 0 };
    int res = zmq_recv(socket, message, 32, ZMQ_DONTWAIT);
    if(res > 0) {
      printf(message); printf("\n");
    }
  }
}
