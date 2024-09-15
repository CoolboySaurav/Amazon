class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        _map_s_t, _map_t_s = {}, {}
        for ch_s, ch_t in zip(s, t):
            if ch_s not in _map_s_t and ch_t not in _map_t_s:
                _map_s_t[ch_s] = ch_t
                _map_t_s[ch_t] = ch_s
            elif _map_s_t.get(ch_s) != ch_t or _map_t_s.get(ch_t) != ch_s:
                return False
        return True