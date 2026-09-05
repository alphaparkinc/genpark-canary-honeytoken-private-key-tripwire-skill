from client import CanaryHoneytokenPrivateKeyTripwireClient

def main():
    client = CanaryHoneytokenPrivateKeyTripwireClient()
    res = client.monitor_honeytoken_mempool_activity()
    print('Canary Honeytoken Tripwire: ' + res['tripwire_session_id'] + ' (' + res['canary_address'] + ')')
    print('Status: ' + res['tripwire_status'] + ' | Tampering: ' + str(res['mempool_tampering_detected']))
    print('Sentinel URL: ' + res['canary_sentinel_url'])

if __name__ == '__main__':
    main()
