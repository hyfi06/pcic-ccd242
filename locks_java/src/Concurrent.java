import java.util.ArrayList;
import java.util.List;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.NoSuchElementException;

public class Concurrent {
  public static void main(String[] args) {
    long startTime = System.currentTimeMillis();

    int threadsNum = 8;
    int length = 1000;

    if (args.length >= 1) {
      try {
        threadsNum = Integer.parseInt(args[0]);
      } catch (NumberFormatException e) {
        System.err.println("Error parsing command line arguments");
        System.exit(1);
      }
    }

    if (args.length >= 2) {
      try {
        length = Integer.parseInt(args[1]);
      } catch (NumberFormatException e) {
        System.err.println("Error parsing command line arguments");
        System.exit(1);
      }
    }

    List<Integer> data = new ArrayList<>();
    for (int i = 0; i < length; i++) {
      data.add(i);
    }

    ConcurrentDispenser<Integer> dispenser = new ConcurrentDispenser<>(data);
    List<Thread> threads = new ArrayList<>();

    for (int i = 0; i < threadsNum; i++) {
      long worker_id = i; // Thread.currentThread().threadId()
      Thread thread = new Thread(() -> worker(dispenser, worker_id));
      thread.start();
      threads.add(thread);
    }

    for (Thread t : threads) {
      try {
        t.join();
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }

    long endTime = System.currentTimeMillis();
    double totalTime = (double) (endTime - startTime) / 1000;
    System.out.println("Tiempo total de ejecución: " + totalTime + " s");
  }

  public static void worker(ConcurrentDispenser<Integer> dispenser, long workerName) {
    int count = 0;
    try {
      while (true) {
        int data = dispenser.next();
        ProofOfWorkResult result = proofOfWork(String.valueOf(data), 4);
        count += 1;
        // System.out.println("Worker " + workerName + ": " + data + " -> " +
        // result.hashResult + " with nonce "
        // + result.nonce + " in " + result.seconds + " s");
      }
    } catch (NoSuchElementException e) {
      // No more elements to process
      System.out.println("Worker " + workerName + " finished: " + count + " works");
    }
  }

  public static ProofOfWorkResult proofOfWork(String inputData, int difficulty) {
    int nonce = 0;
    long startTime = System.currentTimeMillis();
    String target = new String(new char[difficulty]).replace('\0', '0');

    try {
      MessageDigest digest = MessageDigest.getInstance("SHA-256");
      while (true) {
        String inputWithNonce = inputData + nonce;
        byte[] hash = digest.digest(inputWithNonce.getBytes());
        StringBuilder hexString = new StringBuilder();
        for (byte b : hash) {
          String hex = Integer.toHexString(0xff & b);
          if (hex.length() == 1)
            hexString.append('0');
          hexString.append(hex);
        }

        if (hexString.toString().startsWith(target)) {
          long endTime = System.currentTimeMillis();
          float seconds = (endTime - startTime) / 1000F;
          return new ProofOfWorkResult(nonce, hexString.toString(), seconds);
        }

        nonce++;
      }
    } catch (NoSuchAlgorithmException e) {
      throw new RuntimeException(e);
    }
  }

  static class ProofOfWorkResult {
    public final int nonce;
    public final String hashResult;
    public final float seconds;

    public ProofOfWorkResult(int nonce, String hashResult, float seconds) {
      this.nonce = nonce;
      this.hashResult = hashResult;
      this.seconds = seconds;
    }
  }

  static class ConcurrentDispenser<T> {
    private final List<T> data;
    private final Lock lock = new ReentrantLock();

    public ConcurrentDispenser(List<T> data) {
      this.data = data;
    }

    public T next() {
      lock.lock();
      try {
        if (data.isEmpty())
          throw new NoSuchElementException();
        return data.remove(0);
      } finally {
        lock.unlock();
      }
    }
  }
}
