import asyncio
import time

async def main():
    # Create an asyncio event loop
    loop = asyncio.get_event_loop()

    try:
        # Start a timer
        start_time = time.time()

        while True:
            try:
                if shell.recv_ready():
                    output = shell.recv(1024).decode("utf-8")
                    self.__buffer = self.__buffer + output
                    if printFlag:
                        print(output, end="")  # Print without newline
                    if self.__buffer.find("COMMAND FINISHED root") > -1:
                        print("FOUND END of cmd")
                        break
                await asyncio.sleep(0.1)
                
                # Check if 25 seconds have passed
                current_time = time.time()
                if current_time - start_time > 25:
                    print("Time limit reached, breaking the loop.")
                    break

            except KeyboardInterrupt:
                print("\nInterrupt")
                break

    except asyncio.CancelledError:
        print("Task was cancelled.")
    finally:
        loop.close()

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
