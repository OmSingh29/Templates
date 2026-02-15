#define int long long
#define pii pair<int,int>
#define all(x) x.begin(), x.end()

struct SortedList {
    vector<vector<pii>> _lists;
    vector<int> _list_lens;
    vector<pii> _mins;
    vector<int> _fen_tree;
    int _len = 0;
    int _load = 200;
    bool _rebuild = true;

    SortedList(vector<pii> iterable = {}) {
        sort(iterable.begin(), iterable.end());
        _len = iterable.size();
        for (int i = 0; i < _len; i += _load) {
            vector<pii> chunk(iterable.begin() + i, iterable.begin() + min(_len, i + _load));
            _lists.push_back(chunk);
            _list_lens.push_back(chunk.size());
            _mins.push_back(chunk[0]);
        }
    }

    void _fen_build() {
        _fen_tree = _list_lens;
        for (int i = 0; i < (int)_fen_tree.size(); ++i)
            if ((i | (i + 1)) < (int)_fen_tree.size())
                _fen_tree[i | (i + 1)] += _fen_tree[i];
        _rebuild = false;
    }

    void _fen_update(int index, int value) {
        if (!_rebuild) {
            while (index < (int)_fen_tree.size()) {
                _fen_tree[index] += value;
                index |= index + 1;
            }
        }
    }

    int _fen_query(int end) {
        if (_rebuild) _fen_build();
        int x = 0;
        while (end) {
            x += _fen_tree[end - 1];
            end &= end - 1;
        }
        return x;
    }

    pair<int, int> _fen_findkth(int k) {
        if (_list_lens.empty()) return {0, 0};
        if (k < _list_lens[0]) return {0, k};
        if (k >= _len - _list_lens.back()) return {(int)_list_lens.size() - 1, k + _list_lens.back() - _len};
        if (_rebuild) _fen_build();
        int idx = -1;
        for (int d = 63 - __builtin_clzll(_fen_tree.size()); d >= 0; --d) {
            int right_idx = idx + (1LL << d);
            if (right_idx < (int)_fen_tree.size() && k >= _fen_tree[right_idx]) {
                idx = right_idx;
                k -= _fen_tree[idx];
            }
        }
        return {idx + 1, k};
    }

    void _delete(int pos, int idx) {
        _len--;
        _fen_update(pos, -1);
        _lists[pos].erase(_lists[pos].begin() + idx);
        _list_lens[pos]--;
        if (_list_lens[pos]) {
            _mins[pos] = _lists[pos][0];
        } else {
            _lists.erase(_lists.begin() + pos);
            _list_lens.erase(_list_lens.begin() + pos);
            _mins.erase(_mins.begin() + pos);
            _rebuild = true;
        }
    }

    pair<int, int> _loc_left(pii value) {
        if (_lists.empty()) return {0, 0};
        int lo = -1, pos = _lists.size() - 1;
        while (lo + 1 < pos) {
            int mi = (lo + pos) >> 1;
            if (value <= _mins[mi]) pos = mi;
            else lo = mi;
        }
        if (pos && value <= _lists[pos - 1].back()) pos--;
        auto& lst = _lists[pos];
        lo = -1;
        int idx = lst.size();
        while (lo + 1 < idx) {
            int mi = (lo + idx) >> 1;
            if (value <= lst[mi]) idx = mi;
            else lo = mi;
        }
        return {pos, idx};
    }

    pair<int, int> _loc_right(pii value) {
        if (_lists.empty()) return {0, 0};
        int pos = 0, hi = _lists.size();
        while (pos + 1 < hi) {
            int mi = (pos + hi) >> 1;
            if (value < _mins[mi]) hi = mi;
            else pos = mi;
        }
        if (pos >= (int)_lists.size()) return {0, 0};
        auto& lst = _lists[pos];
        int lo = -1, idx = lst.size();
        while (lo + 1 < idx) {
            int mi = (lo + idx) >> 1;
            if (value < lst[mi]) idx = mi;
            else lo = mi;
        }
        return {pos, idx};
    }

    void add(pii value) {
        _len++;
        if (!_lists.empty()) {
            auto [pos, idx] = _loc_right(value);
            if (pos >= (int)_lists.size()) pos = (int)_lists.size() - 1;
            _fen_update(pos, 1);
            _lists[pos].insert(_lists[pos].begin() + idx, value);
            _list_lens[pos]++;
            _mins[pos] = _lists[pos][0];
            if ((int)_lists[pos].size() > _load * 2) {
                vector<pii> new_chunk(_lists[pos].begin() + _load, _lists[pos].end());
                _lists[pos].resize(_load);
                _lists.insert(_lists.begin() + pos + 1, new_chunk);
                _list_lens[pos] = _load;
                _list_lens.insert(_list_lens.begin() + pos + 1, new_chunk.size());
                _mins.insert(_mins.begin() + pos + 1, new_chunk[0]);
                _rebuild = true;
            }
        } else {
            _lists.push_back({value});
            _list_lens.push_back(1);
            _mins.push_back(value);
            _rebuild = true;
        }
    }

    void discard(pii value) {
        if (_lists.empty()) return;
        auto [pos, idx] = _loc_right(value);
        if (pos < (int)_lists.size() && idx > 0 && _lists[pos][idx - 1] == value)
            _delete(pos, idx - 1);
    }

    int bisect_right(pii value) {
        auto [pos, idx] = _loc_right(value);
        return _fen_query(pos) + idx;
    }

    int size() {
        return _len;
    }

    pii operator[](int index) {
        auto [pos, idx] = _fen_findkth(index < 0 ? _len + index : index);
        return _lists[pos][idx];
    }
};
