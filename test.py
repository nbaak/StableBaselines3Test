import time
import torch


def version() -> None:
    print(torch.__version__)
    print(torch.version.hip)  # This should show your ROCm version
    print(torch.cuda.is_available())  # Will return False for ROCm, use hip check instead
    print(torch.backends.mps.is_available())  # Optional, if you also want MPS check

    print(torch.cuda.device_count())  # Usually 0 for ROCm, use hip API
    print(torch.cuda.get_device_name(0))  # Will fail, use torch.cuda or ROCm-specific check


def print_device_info() -> None:
    print("Torch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("ROCm HIP version:", torch.version.hip)

    if torch.cuda.is_available():
        device_count:int = torch.cuda.device_count()
        print("Device count:", device_count)

        for i in range(device_count):
            print(f"Device {i} name:", torch.cuda.get_device_name(i))
    else:
        print("No ROCm-compatible GPU detected.")


def gpu_matrix_test(size:int=4096) -> None:
    if not torch.cuda.is_available():
        print("Skipping GPU test.")
        return

    device:torch.device = torch.device("cuda")
    print(f"\nRunning matrix multiplication test on {device} with size {size}x{size}")

    a:torch.Tensor = torch.randn((size, size), device=device)
    b:torch.Tensor = torch.randn((size, size), device=device)

    torch.cuda.synchronize()
    start:float = time.time()

    c:torch.Tensor = torch.matmul(a, b)

    torch.cuda.synchronize()
    end:float = time.time()

    print("Result tensor device:", c.device)
    print("Computation time:", end - start, "seconds")


def main() -> None:
    version()
    print_device_info()
    gpu_matrix_test()


if __name__ == "__main__":
    main()
