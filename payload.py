import ctypes
import sys
import os

dll_name = "kernel32.dll"
dll_base_address = 0x00400000
dll_base_size = 0x1000

def inject_payload(dll_handle, payload):
    payload_base = payload.base
    payload_size = payload.size
    payload_data = payload.data

    print("Injecting payload into %s at 0x%08x" % (dll_name, dll_base_address))

    c_payload = ctypes.c_void_p(payload_data)
    ctypes.memmove(ctypes.addressof(c_payload), payload_data, payload_size)

    print("Payload injected successfully")

def main():
    dll_handle = ctypes.CDLL(dll_name)
    payload = ctypes.c_char_p("A"*payload_size)
    payload_base = ctypes.cast(payload, ctypes.c_void_p)
    payload_size = ctypes.sizeof(payload)

    inject_payload(dll_handle, payload)

if __name__ == "__main__":
    main()
