#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h> // Para a função sleep

#define NUM_THREADS 100 // Número de threads a serem criadas

void* loop_infinito(void* arg) {
    int thread_id = *((int*)arg);
    while (1) {
        printf("Loop Infinito da Thread %d\n", thread_id);
        //sleep(1);
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];
    int thread_ids[NUM_THREADS];

    // Criar múltiplas threads
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i; // Atribuir um ID à thread
        if (pthread_create(&threads[i], NULL, loop_infinito, (void*)&thread_ids[i]) != 0) {
            perror("Erro ao criar a thread");
            exit(EXIT_FAILURE);
        }
    }

    // Manter o processo principal ativo

    // Juntar as threads (nunca será alcançado neste exemplo)
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
