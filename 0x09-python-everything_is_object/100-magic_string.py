#!/usr/bin/python3
def magic_string(static={"count":}):
    static["count"] += 1
    return str("BestSchool, " * static["count"])[:-2]
