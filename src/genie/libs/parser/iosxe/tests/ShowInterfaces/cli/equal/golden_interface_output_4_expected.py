expected_output = {
    "GigabitEthernet0/0/0": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "auto_negotiate": True,
        "bandwidth": 1000000,
        "counters": {
            "in_broadcast_pkts": 110594334,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 1050221981,
            "in_no_buffer": 0,
            "in_octets": 25781698415464,
            "in_overrun": 0,
            "in_pkts": 37252955968,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 2,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 29981591557915,
            "out_pkts": 35433262342,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 11976504,
            "rate": {
                "in_rate": 10684000,
                "in_rate_pkts": 5031,
                "load_interval": 300,
                "out_rate": 28954000,
                "out_rate_pkts": 5003,
            },
        },
        "delay": 10,
        "description": "Genie to Genie-next for L2 Fiber lines ***",
        "duplex_mode": "full",
        "enabled": True,
        "encapsulations": {"encapsulation": "dot1q", "first_dot1q": "1"},
        "flow_control": {"receive": True, "send": True},
        "last_input": "00:00:00",
        "last_output": "00:00:00",
        "line_protocol": "up",
        "link_type": "auto",
        "mac_address": "1ca1.88ff.c119",
        "media_type": "T",
        "mtu": 1500,
        "oper_status": "up",
        "output_hang": "never",
        "phys_address": "1ca1.88ff.c119",
        "port_channel": {"port_channel_member": False},
        "port_speed": "1000mbps",
        "queues": {
            "input_queue_drops": 9483,
            "input_queue_flushes": 6181,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "Class-based",
            "total_output_drop": 85587314,
        },
        "reliability": "255/255",
        "rxload": "2/255",
        "txload": "7/255",
        "type": "BUILT-IN-EPA-8x1G",
    },
    "GigabitEthernet0/0/0.105": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 100000,
        "delay": 10,
        "description": "Another Genie L2 connection",
        "enabled": True,
        "encapsulations": {"encapsulation": "dot1q", "first_dot1q": "105"},
        "ipv4": {"10.95.2.252/24": {"ip": "10.95.2.252", "prefix_length": "24"}},
        "line_protocol": "up",
        "mac_address": "1ca1.88ff.c119",
        "mtu": 1500,
        "oper_status": "up",
        "phys_address": "1ca1.88ff.c119",
        "port_channel": {"port_channel_member": False},
        "reliability": "255/255",
        "rxload": "2/255",
        "txload": "7/255",
        "type": "BUILT-IN-EPA-8x1G",
    },
    "GigabitEthernet0/0/0.1761524": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 100000,
        "delay": 10,
        "description": "*** Genie VLAN  ***",
        "enabled": True,
        "encapsulations": {
            "encapsulation": "qinq virtual lan",
            "first_dot1q": "176",
            "second_dot1q": "1524",
        },
        "ipv4": {"10.121.113.98/27": {"ip": "10.121.113.98", "prefix_length": "27"}},
        "line_protocol": "up",
        "mac_address": "1ca1.88ff.c119",
        "mtu": 1500,
        "oper_status": "up",
        "phys_address": "1ca1.88ff.c119",
        "port_channel": {"port_channel_member": False},
        "reliability": "255/255",
        "rxload": "2/255",
        "txload": "7/255",
        "type": "BUILT-IN-EPA-8x1G",
    },
}
