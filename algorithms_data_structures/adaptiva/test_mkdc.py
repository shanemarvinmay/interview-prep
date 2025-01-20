import base64

# Retrieve DNS record
def get_dns_record():
    sig_bytes = 'signature'.encode('utf-8')
    return {
        'b':[404],
        'r':[(400,500)],
        's':base64.b64encode(sig_bytes)
    }
# Retieve build number
BUILD_NUM = 1

PUBLIC_KEY = 'signature'

def validate_signature(signature):
    sig = signature.decode('utf-8')
    return sig == 'c2lnbmF0dXJl'

# Check if record is not found - if not found return true
def test_record_found():
    record = get_dns_record() 

    assert record is not None
    assert isinstance(record, dict)

# Validate the signature - if failed return true
def test_signature_validated():
    record = get_dns_record()

    assert 's' in record

    signature = record['s']

    assert validate_signature(signature)

# Check bad build numbers
def test_build_num():
    record = get_dns_record()

    bad_numbers = record.get('b', [])
    bad_numbers.sort()
    bad_ranges = record.get('r', [])
    bad_ranges.sort()

    for bad_num in bad_numbers:
        if BUILD_NUM == bad_num:
            assert False

    for start, end in bad_ranges:
        if start <= BUILD_NUM <= end:
            assert False

# b single numbers
# r for ranges (optional)
# ! can get build number from local client machine !
# Retrun false if unsafe build number
# else true
# true means proceed, false means stop